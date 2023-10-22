package com.example.todo.data_layer.api

import com.example.todo.data_layer.dto.request.ToDoWriteRequest
import com.example.todo.data_layer.dto.response.ToDoApiResponse
import com.example.todo.data_layer.dto.response.ToDoResponse
import com.skydoves.sandwich.ApiResponse
import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.PATCH
import retrofit2.http.POST
import retrofit2.http.Path
import retrofit2.http.Query


interface ToDoRetrofit {
//    @GET("to-do/{userId}")
//    suspend fun getToDoList(
//        @Path("userId") user_id: Int
//    ): ApiResponse<ToDoApiResponse<List<ToDoResponse>>>
//
//    @POST("to-do/{userId}")
//    fun writeToDo(
//        @Path("userId") user_id: Int,
//        @Body toDoWriteRequest: ToDoWriteRequest,
//    ): ApiResponse<ToDoApiResponse<Boolean>>
//
//    @GET("to-do/{userId}/search/")
//    suspend fun searchToDoList(
//        @Path("userId") user_id: Int,
//        @Query("keyword") keyword: String,
//    ): ApiResponse<ToDoApiResponse<List<ToDoResponse>>>
//
//    @PATCH("to-do/complete/{toDoId}")
//    suspend fun updateToDoComplete(
//        @Path("toDoId") toDoId: Int,
//    ): ApiResponse<ToDoApiResponse<Boolean>>
@GET("to-do/{userId}")
suspend fun getToDoList(
    @Path("userId") user_id: Int
): ApiResponse<List<ToDoResponse>>

    @POST("to-do/{userId}")
    fun writeToDo(
        @Path("userId") user_id: Int,
        @Body toDoWriteRequest: ToDoWriteRequest,
    ): ApiResponse<Boolean>

    @GET("to-do/{userId}/search/")
    suspend fun searchToDoList(
        @Path("userId") user_id: Int,
        @Query("keyword") keyword: String,
    ): ApiResponse<List<ToDoResponse>>

    @PATCH("to-do/complete/{toDoId}")
    suspend fun updateToDoComplete(
        @Path("toDoId") toDoId: Int,
    ): ApiResponse<Boolean>
}