package com.example.todo.api

import android.util.Log
import com.example.todo.data.request.ToDoWriteRequest
import com.example.todo.data.response.ToDoResponse
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.flow
import kotlinx.coroutines.flow.flowOn
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import javax.inject.Inject
import kotlin.Exception

class RetrofitRepository @Inject constructor(
    private val retrofitService: RetrofitService
) {
    suspend fun getToDoList(
        user_id: Int
    ): Flow<ApiResponse<List<ToDoResponse>>> = flow {
        try {
            val res = retrofitService.getToDoList(user_id)
            if (res.isSuccessful) {
                res.body()?.let {
                    Log.d("logcat","repository getToDoList: $it")
                    emit(ApiResponse.Success(it))
                }
            }
        } catch (e: Exception) {
            Log.e("logcat", "repository getToDoList error: ${e.printStackTrace()}")
            emit(ApiResponse.Error(e.message!!))
        }
    }.flowOn(Dispatchers.Main.immediate)

    fun writeToDo(
        toDoWriteRequest: ToDoWriteRequest,
    ) {
        retrofitService.writeToDo(1, toDoWriteRequest).enqueue(object : Callback<Any> {
            override fun onResponse(call: Call<Any>, response: Response<Any>) {
                if (response.isSuccessful) {
                    Log.d("logcat", "write success: $response")
                }
            }

            override fun onFailure(call: Call<Any>, t: Throwable) {
                Log.d("logcat", "write fail: $t")
            }
        })
    }

    suspend fun searchToDoList(
        user_id: Int,
        keyword: String,
    ): Flow<ApiResponse<List<ToDoResponse>>> = flow {
        try {
            val res = retrofitService.searchToDoList(user_id = user_id, keyword = keyword)
            if (res.isSuccessful) {
                res.body()?.let {
                    Log.d("logcat","repository searchToDoList: $it")
                    emit(ApiResponse.Success(it))
                }
            }
        } catch (e: Exception) {
            Log.e("logcat", "repository searchToDoList error: ${e.printStackTrace()}")
            emit(ApiResponse.Error(e.message!!))
        }
    }.flowOn(Dispatchers.Main.immediate)

    suspend fun updateToDoComplete(
        to_do_id: Int,
    ): Flow<ApiResponse<Any>> = flow {
        try {
            val res = retrofitService.updateToDoComplete(to_do_id)
            if (res.isSuccessful) {
                res.body()?.let {
                    Log.d("logcat","repository updateComplete: $it")
                    emit(ApiResponse.Success(it))
                }
            }
        } catch (e: Exception) {
            Log.e("logcat", "repository updateComplete error: ${e.printStackTrace()}")
            emit(ApiResponse.Error(e.message!!))
        }
    }.flowOn(Dispatchers.Main.immediate)
}