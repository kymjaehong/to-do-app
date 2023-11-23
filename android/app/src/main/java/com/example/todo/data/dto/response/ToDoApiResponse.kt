package com.example.todo.data.dto.response

import com.google.gson.annotations.SerializedName

data class ToDoApiResponse<T>(
    @SerializedName("status_code")
    val statusCode: Int,

    @SerializedName("message")
    val message: String,

    @SerializedName("data")
    val data: T,
)
