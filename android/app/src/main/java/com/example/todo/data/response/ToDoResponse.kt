package com.example.todo.data.response

data class ToDoResponse(
    val id: Int,
    val content: String,
    val is_complete: Boolean,
    val created: String,
)