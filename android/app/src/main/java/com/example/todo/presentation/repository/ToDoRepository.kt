package com.example.todo.presentation.repository


import android.util.Log
import com.example.todo.data.api.ToDoRetrofit
import com.example.todo.data.dto.request.ToDoWriteRequest
import com.example.todo.data.dto.response.ToDoResponse
import com.example.todo.data.room.ToDoDao
import com.example.todo.utils.DataState
import com.skydoves.sandwich.StatusCode
import com.skydoves.sandwich.message
import com.skydoves.sandwich.suspendOnError
import com.skydoves.sandwich.suspendOnException
import com.skydoves.sandwich.suspendOnSuccess
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.flow

class ToDoRepository(
    //private val toDoDao: ToDoDao,
    private val toDoRetrofit: ToDoRetrofit,
) {
    suspend fun getToDoList(userId: Int): Flow<DataState<List<ToDoResponse>>> =
        flow {
            DataState.Loading
            delay(timeMillis = 1000)
            val response = toDoRetrofit.getToDoList(userId)
            response.suspendOnSuccess {
                /**
                 * dao 처리
                 * remote에서 get한 데이터는
                 * dao에 insert
                 */
                //val networkToDoList = data
                //toDoDao.insert(networkToDoList)
                //val cacheToDoList = toDoDao.get()
                emit(DataState.Success(data.data))
            }
            response.suspendOnError {
                when (statusCode) {
                    StatusCode.Unauthorized -> emit(DataState.OtherError("token time out"))
                    StatusCode.BadGateway -> emit(DataState.OtherError("Something went wrong"))
                    StatusCode.GatewayTimeout -> emit(DataState.OtherError("Unable to fetch data, please try again"))
                    else -> emit(DataState.OtherError(message()))
                }
            }
            response.suspendOnException {
                if (exception.message!!.contains("Unable to resolve host")) {
                    emit(DataState.OtherError("we are unable to process your request, please try again later"))
                } else {
                    Log.e("error", exception.message!!)
                    emit(DataState.Error(exception))
                }
            }
        }

    suspend fun searchToDoList(userId: Int, keyword: String): Flow<DataState<List<ToDoResponse>>> =
        flow {
            DataState.Loading
            delay(timeMillis = 1000)
            val response = toDoRetrofit.searchToDoList(userId, keyword)
            response.suspendOnSuccess {
                /**
                 * dao 처리
                 * remote에서 get한 데이터는
                 * dao에 insert
                 */
                //val networkToDoList = data
                //toDoDao.insert(networkToDoList)
                //val cacheToDoList = toDoDao.get()
                emit(DataState.Success(data.data))
            }
            response.suspendOnError {
                when (statusCode) {
                    StatusCode.Unauthorized -> emit(DataState.OtherError("token time out"))
                    StatusCode.BadGateway -> emit(DataState.OtherError("Something went wrong"))
                    StatusCode.GatewayTimeout -> emit(DataState.OtherError("Unable to fetch data, please try again"))
                    else -> emit(DataState.OtherError(message()))
                }
            }
            response.suspendOnException {
                if (exception.message!!.contains("Unable to resolve host")) {
                    emit(DataState.OtherError("we are unable to process your request, please try again later"))
                } else {
                    Log.e("error", exception.message!!)
                    emit(DataState.Error(exception))
                }
            }
        }

    // post
    fun writeToDo(userId: Int, toDoWriteRequest: ToDoWriteRequest) {
        toDoRetrofit.writeToDo(userId, toDoWriteRequest)
    }

    suspend fun updateToDoComplete(toDoId: Int) {
        // dao 처리
        toDoRetrofit.updateToDoComplete(toDoId)
    }

}