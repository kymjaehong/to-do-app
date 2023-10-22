package com.example.todo.presentation_layer.viewmodel

import android.util.Log
import androidx.lifecycle.SavedStateHandle
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.todo.api.ApiState
import com.example.todo.api.RetrofitRepository
import com.example.todo.data_layer.dto.response.ToDoResponse
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.catch
import kotlinx.coroutines.launch
import javax.inject.Inject

@HiltViewModel
class ListViewModel @Inject constructor(
    private val retrofitRepository: RetrofitRepository,
    private val savedStateHandle: SavedStateHandle,

    ): ViewModel() {

    private val _toDoList = MutableStateFlow<ApiState<List<ToDoResponse>>>(ApiState.Loading())
    val todoList = _toDoList.asStateFlow()

    fun getToDoList(user_id: Int) {
        viewModelScope.launch {
            retrofitRepository.getToDoList(user_id)
                .catch { error ->
                    _toDoList.value = ApiState.Error(error.message!!)
                }
                .collect { values ->
                    Log.d("logcat","listViewModel getToDoList call")
                    _toDoList.value = values
            }
        }
    }

    fun toLoadingApiResponse() {
        _toDoList.value = ApiState.Loading()
        Log.d("logcat","set apiResponse loading")
    }

}