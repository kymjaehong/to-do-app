package com.example.todo.presentation_layer.viewmodel

import androidx.lifecycle.SavedStateHandle
import androidx.lifecycle.ViewModel
import com.example.todo.api.RetrofitRepository
import com.example.todo.data_layer.dto.request.ToDoWriteRequest
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