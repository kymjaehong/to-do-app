package com.example.todo.ui.viewmodel

import androidx.lifecycle.ViewModel
import com.example.todo.data.dto.request.ToDoWriteRequest
import com.example.todo.presentation.repository.ToDoRepository
import dagger.hilt.android.lifecycle.HiltViewModel
import javax.inject.Inject

@HiltViewModel
class WriteViewModel @Inject constructor(
    private val toDoRepository: ToDoRepository
): ViewModel() {
    // view model logic
    fun writeToDo(
        userId: Int,
        toDoWriteRequest: ToDoWriteRequest,
    ) {
        toDoRepository.writeToDo(userId, toDoWriteRequest)
    }

}