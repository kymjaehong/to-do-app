package com.example.todo

import com.example.todo.data.response.ToDoResponse
import retrofit2.Call
import retrofit2.http.FieldMap
import retrofit2.http.FormUrlEncoded
import retrofit2.http.GET
import retrofit2.http.HeaderMap
import retrofit2.http.POST
import retrofit2.http.PUT
import retrofit2.http.Path
import retrofit2.http.Query

interface RetrofitService {
    @POST("to-do/")
    @FormUrlEncoded
    fun makeToDo(
        @HeaderMap header: HashMap<String, String>,
        @FieldMap params: HashMap<String, Any>
    ): Call<Any>

    @GET("to-do/{user_id}")
    fun getToDoList(
        //@HeaderMap header: HashMap<String, String>,
        @Path("user_id") user_id: Int
    ): Call<ArrayList<ToDoResponse>>

    @PUT("to-do/complete/{toDoId}")
    fun changeToDoComplete(
        @HeaderMap header: HashMap<String, String>,
        @Path("toDoId") toDoId: Int,
    ): Call<Any>

    @GET("to-do/search/")
    fun searchToDoList(
        @HeaderMap header: HashMap<String, String>,
        @Query("keyword") keyword: String
    ): Call<ArrayList<ToDoResponse>>
}