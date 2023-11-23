package com.example.todo.ui.viewmodel

import android.util.Log
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.todo.data.dto.response.ToDoResponse
import com.example.todo.presentation.repository.ToDoRepository
import com.example.todo.utils.DataState
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.catch
import kotlinx.coroutines.launch
import javax.inject.Inject

@HiltViewModel
class ListViewModel @Inject constructor(
    private val toDoRepository: ToDoRepository
    ): ViewModel() {

    private val _toDoList = MutableStateFlow<DataState<List<ToDoResponse>>>(DataState.Loading)
    val todoList = _toDoList.asStateFlow()

    fun getToDoList(user_id: Int) {
        viewModelScope.launch {
            toDoRepository.getToDoList(user_id)
                .catch { error ->
                    _toDoList.value = DataState.Error(error)
                }
                .collect { values ->
                    Log.d("logcat","listViewModel getToDoList call")
                    _toDoList.value = values
                }
        }
    }

    fun toLoadingApiResponse() {
        _toDoList.value = DataState.Loading
        Log.d("logcat","set apiResponse loading")
    }

}