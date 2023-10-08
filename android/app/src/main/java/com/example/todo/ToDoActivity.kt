package com.example.todo

import android.content.Intent
import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import androidx.activity.viewModels
import androidx.core.widget.doAfterTextChanged
import androidx.lifecycle.Lifecycle
import androidx.lifecycle.lifecycleScope
import androidx.lifecycle.repeatOnLifecycle
import androidx.recyclerview.widget.RecyclerView
import com.example.todo.api.ApiResponse
import com.example.todo.databinding.ActivityToDoBinding
import com.example.todo.ui.BaseActivity
import com.example.todo.viewmodel.ListViewModel
import dagger.hilt.android.AndroidEntryPoint
import kotlinx.coroutines.launch
import com.example.todo.ui.adapter.ToDoListRecyclerViewAdapter
import com.example.todo.viewmodel.SearchViewModel
import com.example.todo.viewmodel.UpdateViewModel

@AndroidEntryPoint
class ToDoActivity : BaseActivity() {

    override val binding by lazy {
        ActivityToDoBinding.inflate(layoutInflater)
    }

    private val listViewModel by viewModels<ListViewModel>()
    private val searchViewModel by viewModels<SearchViewModel>()
    private val updateViewModel by viewModels<UpdateViewModel>()

    lateinit var toDoRecyclerView: RecyclerView
    var searchQuery: String = ""

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // get to-do list
        toDoRecyclerView = binding.todoList
        lifecycleScope.launch {
            lifecycle.repeatOnLifecycle(Lifecycle.State.STARTED) {
                listViewModel.apply {
                    /**
                     * 로그인 기능 추가 시,
                     * 인자: 내 계정 id
                     */
                    getToDoList(1)

                    todoList.collect { apiResponse ->
                        when (apiResponse) {
                            is ApiResponse.Success -> {
                                apiResponse.data?.let { values ->
                                    Log.d("logcat","todo activity: $values")
                                    toDoRecyclerView.adapter = ToDoListRecyclerViewAdapter(
                                        values,
                                        LayoutInflater.from(this@ToDoActivity),
                                        this@ToDoActivity
                                    )
                                }
                                toLoadingApiResponse()
                            }
                            is ApiResponse.Error -> {
                                Log.e("logcat", "${apiResponse.message}")
                                toLoadingApiResponse()
                            }
                            is ApiResponse.Loading -> {}
                        }
                    }
                }
            }
        }

        // to-do write
        binding.write.setOnClickListener {
            startActivity(Intent(this, ToDoWriteActivity::class.java))
        }

        // search to-do
        binding.searchEdittext.doAfterTextChanged {
            searchQuery = it.toString()
        }
        binding.searchBtn.setOnClickListener {
            lifecycleScope.launch {
                lifecycle.repeatOnLifecycle(Lifecycle.State.STARTED) {
                    clickSearchBtn()
                }
            }
        }
    }

    private suspend fun clickSearchBtn() {
        searchViewModel.apply {
            /**
             * 로그인 기능 추가 시,
             * 인자: 내 계정 id
             */
            searchToDoList(1, searchQuery)

            searchTodoList.collect { apiResponse ->
                when (apiResponse) {
                    is ApiResponse.Success -> {
                        apiResponse.data?.let { values ->
                            toDoRecyclerView.adapter = ToDoListRecyclerViewAdapter(
                                values,
                                LayoutInflater.from(this@ToDoActivity),
                                this@ToDoActivity
                            )
                        }
                        toLoadingApiResponse()
                    }

                    is ApiResponse.Error -> {
                        Log.e("logcat", "${apiResponse.message}")
                        toLoadingApiResponse()
                    }

                    is ApiResponse.Loading -> {}
                }
            }
        }
    }


    fun updateToDoComplete(to_do_id: Int) {
        lifecycleScope.launch {
            lifecycle.repeatOnLifecycle(Lifecycle.State.STARTED) {
                updateViewModel.apply {
                    updateToDoList(to_do_id)
                    updateTodoList.collect { apiResponse ->
                        when (apiResponse) {
                            is ApiResponse.Success -> {}
                            is ApiResponse.Error -> {
                                Log.e("logcat", "${apiResponse.message}")
                                toLoadingApiResponse()
                            }
                            is ApiResponse.Loading -> {
                                Log.d("logcat", "update complete after~")
                                clickSearchBtn()
                            }
                        }
                    }
                }
            }
        }
    }
}