package com.example.todo.data_layer.dto.response

import com.google.gson.annotations.SerializedName

data class ToDoResponse(
    @SerializedName("id")
    val id: Int,
    @SerializedName("content")
    val content: String,
    @SerializedName("is_complete")
    val isComplete: Boolean,
    @SerializedName("created")
    val created: String,
)