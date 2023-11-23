package com.example.todo.ui

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
import com.example.todo.databinding.ActivityToDoBinding
import com.example.todo.ui.viewmodel.ListViewModel
import dagger.hilt.android.AndroidEntryPoint
import kotlinx.coroutines.launch
import com.example.todo.ui.adapter.ToDoListRecyclerViewAdapter
import com.example.todo.ui.viewmodel.SearchViewModel
import com.example.todo.ui.viewmodel.UpdateViewModel
import com.example.todo.utils.DataState

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

                    todoList.collect { dataState ->
                        when (dataState) {
                            is DataState.Success -> {
                                Log.d("logcat","todo activity: $dataState")
                                toDoRecyclerView.adapter = ToDoListRecyclerViewAdapter(
                                    dataState.data,
                                    LayoutInflater.from(this@ToDoActivity),
                                    this@ToDoActivity
                                )
                            }
                            is DataState.Error -> {
                                Log.e("error", "${dataState.exception}")
                            }
                            is DataState.OtherError -> {}
                            is DataState.Loading -> {}
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
                lifecycle.repeatOnLifecycle(Lifecycle.State.RESUMED) {
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

            searchTodoList.collect { dataState ->
                when (dataState) {
                    is DataState.Success -> {
                        toDoRecyclerView.adapter = ToDoListRecyclerViewAdapter(
                            dataState.data,
                            LayoutInflater.from(this@ToDoActivity),
                            this@ToDoActivity
                        )
                    }
                    is DataState.Error -> {
                        Log.e("error", "${dataState.exception}")
                    }
                    is DataState.OtherError -> {}
                    is DataState.Loading -> {}
                }
            }
        }
    }


    fun updateToDoComplete(to_do_id: Int) {
        lifecycleScope.launch {
            lifecycle.repeatOnLifecycle(Lifecycle.State.RESUMED) {
                updateViewModel.apply {
                    updateToDoList(to_do_id)
                    updateTodoList.collect { dataState ->
                        when (dataState) {
                            is DataState.Success -> {
                                // 성공 후, 화면 재 호출
                                clickSearchBtn()
                            }
                            is DataState.Error -> {}
                            is DataState.OtherError -> {}
                            is DataState.Loading -> {}
                        }
                    }
                }
            }
        }
    }
}