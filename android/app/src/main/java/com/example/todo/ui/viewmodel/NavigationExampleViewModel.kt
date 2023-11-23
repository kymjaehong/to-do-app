package com.example.todo.ui.viewmodel

import androidx.lifecycle.SavedStateHandle
import androidx.lifecycle.ViewModel
import com.example.todo.presentation.repository.ToDoRepository
import dagger.hilt.android.lifecycle.HiltViewModel
import javax.inject.Inject

@HiltViewModel
class NavigationExampleViewModel @Inject constructor(
    private val toDoRepository: ToDoRepository
): ViewModel() {
    // view model logic
}