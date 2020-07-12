package com.example.demo.controller

import com.example.demo.model.User
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RequestParam
import org.springframework.web.bind.annotation.RestController

@RestController
class UserController {

    @GetMapping("/user")
    fun getUser(@RequestParam(value = "firstname", defaultValue = "Khanh") firstname: String): User {
        return User(firstname)
    }

    @PostMapping("/user")
    fun postUser(user: User): User {
        return user
    }
}