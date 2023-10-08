package com.example.todo.viewmodel

import androidx.lifecycle.SavedStateHandle
import androidx.lifecycle.ViewModel
import com.example.todo.ToDoWriteActivity
import com.example.todo.api.RetrofitRepository
import com.example.todo.data.request.ToDoWriteRequest
import dagger.hilt.android.lifecycle.HiltViewModel
import javax.inject.Inject

@HiltViewModel
class WriteViewModel @Inject constructor(
    private val retrofitRepository: RetrofitRepository,
    private val savedStateHandle: SavedStateHandle,
): ViewModel() {
    // view model logic
    fun writeToDo(
        toDoWriteRequest: ToDoWriteRequest,
    ) {
        retrofitRepository.writeToDo(toDoWriteRequest)
    }

}