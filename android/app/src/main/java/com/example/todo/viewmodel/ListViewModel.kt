package com.example.todo.viewmodel

import android.util.Log
import androidx.lifecycle.SavedStateHandle
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.todo.api.ApiResponse
import com.example.todo.api.RetrofitRepository
import com.example.todo.data.response.ToDoResponse
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.catch
import kotlinx.coroutines.launch
import javax.inject.Inject

@HiltViewModel
class ListViewModel @Inject constructor(
    private val retrofitRepository: RetrofitRepository,
    private val savedStateHandle: SavedStateHandle,

    ): ViewModel() {

    private val _toDoList = MutableStateFlow<ApiResponse<ArrayList<ToDoResponse>>>(ApiResponse.Loading())
    val todoList: StateFlow<ApiResponse<ArrayList<ToDoResponse>>> = _toDoList

    fun getToDoList(user_id: Int) {
        viewModelScope.launch {
            retrofitRepository.getToDoList(user_id)
                .catch { error ->
                    _toDoList.value = ApiResponse.Error(error.message!!)
                }
                .collect { values ->
                    Log.d("logcat","listViewModel getToDoList call")
                    _toDoList.value = values
            }
        }
    }

    fun toLoadingApiResponse() {
        _toDoList.value = ApiResponse.Loading()
        Log.d("logcat","set apiResponse loading")
    }

}