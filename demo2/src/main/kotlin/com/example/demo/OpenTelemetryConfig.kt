package com.example.demo

import io.opentelemetry.api.OpenTelemetry
import io.opentelemetry.api.common.AttributeKey
import io.opentelemetry.api.common.Attributes
import io.opentelemetry.api.trace.SpanKind
import io.opentelemetry.api.trace.StatusCode
import io.opentelemetry.api.trace.Tracer
import io.opentelemetry.exporter.otlp.trace.OtlpGrpcSpanExporter
import io.opentelemetry.sdk.OpenTelemetrySdk
import io.opentelemetry.sdk.resources.Resource
import io.opentelemetry.sdk.trace.SdkTracerProvider
import io.opentelemetry.sdk.trace.export.BatchSpanProcessor
import org.springframework.beans.factory.annotation.Value
import org.springframework.boot.web.servlet.FilterRegistrationBean
import org.springframework.context.annotation.Bean
import org.springframework.context.annotation.Configuration
import org.springframework.web.filter.OncePerRequestFilter
import javax.servlet.FilterChain
import javax.servlet.http.HttpServletRequest
import javax.servlet.http.HttpServletResponse

@Configuration
class OpenTelemetryConfig(
    @Value("\${otel.exporter.otlp.endpoint:http://localhost:4317}")
    private val otlpEndpoint: String,
    @Value("\${otel.service.name:demo2}")
    private val serviceName: String,
    @Value("\${otel.service.namespace:legacy-migration}")
    private val serviceNamespace: String,
    @Value("\${otel.service.version:0.0.1}")
    private val serviceVersion: String
) {

    @Bean
    fun openTelemetry(): OpenTelemetry {
        val resource = Resource.create(
            Attributes.builder()
                .put(AttributeKey.stringKey("service.name"), serviceName)
                .put(AttributeKey.stringKey("service.namespace"), serviceNamespace)
                .put(AttributeKey.stringKey("service.version"), serviceVersion)
                .build()
        )

        val spanExporter = OtlpGrpcSpanExporter.builder()
            .setEndpoint(otlpEndpoint)
            .build()

        val tracerProvider = SdkTracerProvider.builder()
            .setResource(resource)
            .addSpanProcessor(BatchSpanProcessor.builder(spanExporter).build())
            .build()

        val openTelemetry = OpenTelemetrySdk.builder()
            .setTracerProvider(tracerProvider)
            .buildAndRegisterGlobal()

        Runtime.getRuntime().addShutdownHook(Thread {
            tracerProvider.shutdown()
        })

        return openTelemetry
    }

    @Bean
    fun tracer(openTelemetry: OpenTelemetry): Tracer {
        return openTelemetry.getTracer(serviceName, serviceVersion)
    }

    @Bean
    fun openTelemetryFilterRegistration(tracer: Tracer): FilterRegistrationBean<OpenTelemetryFilter> {
        val registrationBean = FilterRegistrationBean(OpenTelemetryFilter(tracer))
        registrationBean.order = 0
        registrationBean.addUrlPatterns("/*")
        return registrationBean
    }

    class OpenTelemetryFilter(private val tracer: Tracer) : OncePerRequestFilter() {
        override fun doFilterInternal(
            request: HttpServletRequest,
            response: HttpServletResponse,
            filterChain: FilterChain
        ) {
            val spanName = "${request.method} ${request.requestURI}"
            val span = tracer.spanBuilder(spanName)
                .setSpanKind(SpanKind.SERVER)
                .setAttribute(AttributeKey.stringKey("http.method"), request.method)
                .setAttribute(AttributeKey.stringKey("http.scheme"), request.scheme)
                .setAttribute(AttributeKey.stringKey("http.host"), request.serverName)
                .setAttribute(AttributeKey.stringKey("http.target"), request.requestURI)
                .setAttribute(AttributeKey.stringKey("http.user_agent"), request.getHeader("User-Agent") ?: "")
                .setAttribute(AttributeKey.stringKey("http.flavor"), request.protocol)
                .startSpan()

            val scope = span.makeCurrent()
            try {
                filterChain.doFilter(request, response)
                span.setAttribute(AttributeKey.longKey("http.status_code"), response.status.toLong())
                if (response.status >= 500) {
                    span.setStatus(StatusCode.ERROR)
                }
            } catch (error: Exception) {
                span.recordException(error)
                span.setStatus(StatusCode.ERROR)
                throw error
            } finally {
                scope.close()
                span.end()
            }
        }
    }
}
