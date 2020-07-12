package com.example.demo

import org.springframework.beans.factory.annotation.Autowired
import org.springframework.context.ApplicationContext
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
import org.thymeleaf.spring5.SpringTemplateEngine
import org.thymeleaf.spring5.templateresolver.SpringResourceTemplateResolver
import org.thymeleaf.spring5.view.ThymeleafViewResolver
import java.util.*

@Configuration
class DemoConfig:WebMvcConfigurer {

    @Autowired
    private lateinit var applicationContext: ApplicationContext

    @Bean
    fun viewResolver(): ViewResolver{
        val bean = InternalResourceViewResolver()
        bean.setPrefix("/webapp/WEB-INF/jsp/")
        bean.setSuffix(".jsp")
        bean.order = 1
        return bean
    }

    override fun addResourceHandlers(registry: ResourceHandlerRegistry) {
        registry.addResourceHandler("/files/**").addResourceLocations("/webapp/WEB-INF/pdf/")
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

    @Bean
    fun templateResolver(): SpringResourceTemplateResolver {
        val templateResolver = SpringResourceTemplateResolver()
        templateResolver.setApplicationContext(applicationContext)
        templateResolver.prefix = "/WEB-INF/views/"
        templateResolver.suffix = ".html"
        return templateResolver
    }

    @Bean
    fun templateEngine(): SpringTemplateEngine {
        val templateEngine = SpringTemplateEngine()
        templateEngine.setTemplateResolver(templateResolver())
        templateEngine.enableSpringELCompiler = true
        return templateEngine
    }

    @Bean
    fun thymeleafResolver(): ViewResolver{
        val viewResolver = ThymeleafViewResolver()
        viewResolver.templateEngine = templateEngine()
        viewResolver.order = 0
        return viewResolver
    }
}