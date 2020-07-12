package com.example.demo

import org.springframework.beans.factory.annotation.Configurable
import org.springframework.context.annotation.Bean
import org.springframework.context.annotation.Configuration
import org.springframework.web.servlet.ViewResolver
import org.springframework.web.servlet.view.InternalResourceViewResolver

@Configuration
class DemoConfig {

    @Bean
    fun viewResolver(): ViewResolver{
        val bean = InternalResourceViewResolver()
        bean.setPrefix("/WEB-INF/jsp/")
        bean.setSuffix(".jsp")
        bean.order = 0
        return bean
    }


}