package com.example.todo.viewmodel

import androidx.lifecycle.SavedStateHandle
import androidx.lifecycle.ViewModel
import com.example.todo.api.RetrofitRepository
import dagger.hilt.android.lifecycle.HiltViewModel
import javax.inject.Inject

@HiltViewModel
class NavigationExampleViewModel @Inject constructor(
    private val retrofitRepository: RetrofitRepository,
    private val savedStateHandle: SavedStateHandle,
): ViewModel() {
    // view model logic
}