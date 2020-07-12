package com.example.demo.controller

import org.springframework.stereotype.Controller
import org.springframework.web.bind.annotation.GetMapping

@Controller
class RegistrationController {
    @GetMapping("registration")
    fun registration(model: Map<String, Any>) : String{
        return "registration"
    }
}