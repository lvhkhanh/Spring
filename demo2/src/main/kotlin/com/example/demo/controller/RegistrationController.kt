package com.example.demo.controller

import com.example.demo.model.Registration
import org.springframework.stereotype.Controller
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.ModelAttribute
import org.springframework.web.bind.annotation.PostMapping

@Controller
class RegistrationController {
    @GetMapping("registration")
    fun registration(@ModelAttribute("registration") registration: Registration) : String{
        return "registration"
    }

    @PostMapping("registration")
    fun addRegistration(@ModelAttribute("registration") registration: Registration) : String{
//        TODO: add logger
        println(registration)
        return "redirect:registration"
    }
}