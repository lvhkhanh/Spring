package com.example.demo.model

import javax.validation.constraints.NotEmpty

data class Registration(@NotEmpty var name: String)