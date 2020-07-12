package com.example.demo

import org.apache.tomcat.util.descriptor.LocalResolver
import org.springframework.beans.factory.annotation.Configurable
import org.springframework.context.annotation.Bean
import org.springframework.context.annotation.Configuration
import org.springframework.web.servlet.LocaleResolver
import org.springframework.web.servlet.ViewResolver
import org.springframework.web.servlet.config.annotation.InterceptorRegistry
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer
import org.springframework.web.servlet.i18n.LocaleChangeInterceptor
import org.springframework.web.servlet.i18n.SessionLocaleResolver
import org.springframework.web.servlet.view.InternalResourceViewResolver
import java.util.*

@Configuration
class DemoConfig:WebMvcConfigurer {

    @Bean
    fun viewResolver(): ViewResolver{
        val bean = InternalResourceViewResolver()
        bean.setPrefix("/WEB-INF/jsp/")
        bean.setSuffix(".jsp")
        bean.order = 0
        return bean
    }

    override fun addResourceHandlers(registry: ResourceHandlerRegistry) {
        registry.addResourceHandler("/files/**").addResourceLocations("/WEB-INF/pdf/")
    }

    @Bean
    fun localeResolver(): LocaleResolver {
        val sessionLocalResolver = SessionLocaleResolver()
        sessionLocalResolver.setDefaultLocale(Locale.US)
        return  sessionLocalResolver
    }

    @Bean
    fun localeChangeInterceptor(): LocaleChangeInterceptor{
        val localeChangeInterceptor = LocaleChangeInterceptor()
        localeChangeInterceptor.paramName = "lang"
        return  localeChangeInterceptor
    }

    override fun addInterceptors(registry: InterceptorRegistry) {
        registry.addInterceptor(localeChangeInterceptor())
    }
}