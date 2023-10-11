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
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.catch
import kotlinx.coroutines.flow.collectLatest
import kotlinx.coroutines.launch
import javax.inject.Inject

@HiltViewModel
class SearchViewModel @Inject constructor(
    private val retrofitRepository: RetrofitRepository,
    private val savedStateHandle: SavedStateHandle,

    ): ViewModel() {

    private val _searchToDoList = MutableStateFlow<ApiResponse<List<ToDoResponse>>>(ApiResponse.Loading())
    val searchTodoList = _searchToDoList.asStateFlow()

    fun searchToDoList(user_id: Int, keyword: String) {
        viewModelScope.launch {
            retrofitRepository.searchToDoList(user_id = user_id, keyword = keyword)
                .catch { error ->
                    _searchToDoList.value = ApiResponse.Error(error.message!!)
                }
                .collectLatest { values ->
                    Log.d("logcat","listViewModel getToDoList call")
                    _searchToDoList.value = values
            }
        }
    }

    fun toLoadingApiResponse() {
        _searchToDoList.value = ApiResponse.Loading()
        Log.d("logcat","set apiResponse loading")
    }

}