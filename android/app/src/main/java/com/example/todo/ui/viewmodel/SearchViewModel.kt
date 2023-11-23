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
import kotlinx.coroutines.flow.collectLatest
import kotlinx.coroutines.launch
import javax.inject.Inject

@HiltViewModel
class SearchViewModel @Inject constructor(
    private val toDoRepository: ToDoRepository
    ): ViewModel() {

    private val _searchToDoList = MutableStateFlow<DataState<List<ToDoResponse>>>(DataState.Loading)
    val searchTodoList = _searchToDoList.asStateFlow()

    fun searchToDoList(userId: Int, keyword: String) {
        viewModelScope.launch {
            toDoRepository.searchToDoList(userId, keyword)
                .catch { error ->
                    _searchToDoList.value = DataState.Error(error)
                }
                .collect { values ->
                    Log.d("logcat","listViewModel getToDoList call")
                    _searchToDoList.value = values
            }
        }
    }

    fun toLoadingApiResponse() {
        _searchToDoList.value = DataState.Loading
        Log.d("logcat","set apiResponse loading")
    }

}