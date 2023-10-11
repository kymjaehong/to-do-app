package com.example.todo.viewmodel

import android.util.Log
import androidx.lifecycle.SavedStateHandle
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.todo.api.ApiResponse
import com.example.todo.api.RetrofitRepository
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.catch
import kotlinx.coroutines.flow.flowOn
import kotlinx.coroutines.launch
import javax.inject.Inject

@HiltViewModel
class UpdateViewModel @Inject constructor(
    private val retrofitRepository: RetrofitRepository,
    private val savedStateHandle: SavedStateHandle,

    ): ViewModel() {

    private val _updateToDoList = MutableStateFlow<ApiResponse<Any>>(ApiResponse.Loading())
    val updateTodoList: StateFlow<ApiResponse<Any>> = _updateToDoList

    fun updateToDoList(to_do_id: Int) {
        viewModelScope.launch {
            retrofitRepository.updateToDoComplete(to_do_id = to_do_id)
                .flowOn(Dispatchers.Main.immediate)
                .catch { error ->
                    Log.e("logcat","updateViewModel $error")
                    _updateToDoList.value = ApiResponse.Error(error.message!!)
                }
                .collect { values ->
                    Log.d("logcat","updateViewModel updateToDoList call")
                    _updateToDoList.value = values
                }
            Log.d("logcat","updateViewModel updateToDoList call")
        }
    }

    fun toLoadingApiResponse() {
        _updateToDoList.value = ApiResponse.Loading()
        Log.d("logcat","set apiResponse loading")
    }

}