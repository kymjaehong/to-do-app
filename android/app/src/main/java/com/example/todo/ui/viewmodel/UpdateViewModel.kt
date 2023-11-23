package com.example.todo.ui.viewmodel

import android.util.Log
import androidx.lifecycle.ViewModel
import com.example.todo.presentation.repository.ToDoRepository
import com.example.todo.utils.DataState
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.asStateFlow
import javax.inject.Inject

@HiltViewModel
class UpdateViewModel @Inject constructor(
    private val toDoRepository: ToDoRepository
    ): ViewModel() {

    private val _updateToDoList = MutableStateFlow<DataState<Unit>>(DataState.Loading)
    val updateTodoList = _updateToDoList.asStateFlow()

    suspend fun updateToDoList(toDoId: Int) {
        toDoRepository.updateToDoComplete(toDoId)
    }

    fun toLoadingApiResponse() {
        _updateToDoList.value = DataState.Loading
        Log.d("logcat","set apiResponse loading")
    }

}