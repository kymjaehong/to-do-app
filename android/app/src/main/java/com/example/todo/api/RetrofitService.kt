package com.example.todo.api

import com.example.todo.data.request.ToDoWriteRequest
import com.example.todo.data.response.ToDoResponse
import retrofit2.Call
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.PATCH
import retrofit2.http.POST
import retrofit2.http.Path
import retrofit2.http.Query

private const val currVersion = "v1/"

interface RetrofitService {

    @GET("to-do/{user_id}")
    suspend fun getToDoList(
        @Path("user_id") user_id: Int
    ): Response<List<ToDoResponse>>

    @POST("to-do/{user_id}")
    fun writeToDo(
        @Path("user_id") user_id: Int,
        @Body toDoWriteRequest: ToDoWriteRequest,
    ): Call<Any>

    @GET("to-do/{user_id}/search/")
    suspend fun searchToDoList(
        @Path("user_id") user_id: Int,
        @Query("keyword") keyword: String,
    ): Response<List<ToDoResponse>>

    @PATCH("to-do/complete/{toDoId}")
    suspend fun updateToDoComplete(
        @Path("toDoId") toDoId: Int,
    ): Response<Any>

    companion object {
        private const val BASE_URL = "http://10.0.2.2:8000/api/$currVersion"

        fun create(): RetrofitService {
            return Retrofit.Builder()
                .baseUrl(BASE_URL)
                .addConverterFactory(GsonConverterFactory.create())
                .build()
                .create(RetrofitService::class.java)
        }
    }
}