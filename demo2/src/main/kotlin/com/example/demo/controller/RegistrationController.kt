package com.example.demo.controller

import com.example.demo.model.Registration
import org.springframework.stereotype.Controller
import org.springframework.ui.ModelMap
import org.springframework.validation.BindingResult
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.ModelAttribute
import org.springframework.web.bind.annotation.PostMapping
import javax.validation.Valid

@Controller
class RegistrationController {
    @GetMapping("registration")
    fun registration(@ModelAttribute("registration") registration: Registration) : String{
        return "registration"
    }

    @PostMapping("registration")
    fun addRegistration(@Valid @ModelAttribute("registration") registration: Registration, bindingResult: BindingResult, modelMap: ModelMap) : String{
//        TODO: add logger
        if (bindingResult.hasErrors()) {
            return "registration"
        }
        return "redirect:registration"
    }
}