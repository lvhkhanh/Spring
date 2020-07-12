package com.example.demo.controller

import org.springframework.stereotype.Controller
import org.springframework.web.bind.annotation.GetMapping

@Controller
class FirstController {
    @GetMapping("/first")
    fun first(model: Map<String, Any>): String {
        model.plus(Pair("message", "message from controller"))
        return "first"
    }
}