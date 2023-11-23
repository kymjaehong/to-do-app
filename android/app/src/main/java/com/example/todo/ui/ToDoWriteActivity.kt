package com.example.todo.ui

import android.os.Bundle
import android.util.Log
import androidx.activity.viewModels
import androidx.core.widget.doAfterTextChanged
import com.example.todo.data.dto.request.ToDoWriteRequest
import com.example.todo.databinding.ActivityToDoWriteBinding
import com.example.todo.ui.viewmodel.WriteViewModel
import dagger.hilt.android.AndroidEntryPoint

@AndroidEntryPoint
class ToDoWriteActivity: BaseActivity() {

    override val binding by lazy {
        ActivityToDoWriteBinding.inflate(layoutInflater)
    }

    private val writeViewModel by viewModels<WriteViewModel>()

    var content: String = ""

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        binding.contentEdittext.doAfterTextChanged {
            content = it.toString()
        }

        binding.makeTodo.setOnClickListener {
            Log.d("logcat", "write activity call")
            val header = hashMapOf<String, String>()
            header["Authorization"] = "token " + "de3cc238e1e129ed0aec8ae60dd55b022fb41d11"

            Log.d("logcat", "content: $content")
            val toDoWriteRequest = ToDoWriteRequest(content)

            writeViewModel.writeToDo(1, toDoWriteRequest)
            backPressed()
        }
    }

    private fun backPressed() {
        Log.d("logcat", "뒤로 가기 실행")
        this.onBackPressedDispatcher.onBackPressed()
    }
}