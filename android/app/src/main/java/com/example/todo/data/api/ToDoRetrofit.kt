package com.example.todo.data.api

import com.example.todo.data.dto.request.ToDoWriteRequest
import com.example.todo.data.dto.response.ToDoApiResponse
import com.example.todo.data.dto.response.ToDoResponse
import com.skydoves.sandwich.ApiResponse
import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.PATCH
import retrofit2.http.POST
import retrofit2.http.Path
import retrofit2.http.Query


interface ToDoRetrofit {
    @GET("todo/{userId}")
    suspend fun getToDoList(
        @Path("userId") user_id: Int
    ): ApiResponse<ToDoApiResponse<List<ToDoResponse>>>

    @GET("todo/{userId}/search/")
    suspend fun searchToDoList(
        @Path("userId") user_id: Int,
        @Query("keyword") keyword: String,
    ): ApiResponse<ToDoApiResponse<List<ToDoResponse>>>

    @POST("todo/{userId}")
    fun writeToDo(
        @Path("userId") user_id: Int,
        @Body toDoWriteRequest: ToDoWriteRequest,
    ): ApiResponse<ToDoApiResponse<Boolean>>

    @PATCH("todo/complete/{toDoId}")
    suspend fun updateToDoComplete(
        @Path("toDoId") toDoId: Int,
    ): ApiResponse<ToDoApiResponse<Boolean>>
}