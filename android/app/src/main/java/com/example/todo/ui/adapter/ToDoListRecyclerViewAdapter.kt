package com.example.todo.ui.adapter

import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.example.todo.R
import com.example.todo.ui.ToDoActivity
import com.example.todo.data.dto.response.ToDoResponse

class ToDoListRecyclerViewAdapter(
    val toDoList: List<ToDoResponse>,
    val inflater: LayoutInflater,
    val activity: ToDoActivity,
) : RecyclerView.Adapter<RecyclerView.ViewHolder>() {
    // 날짜 구분을 위한 변수
    var previousDate: String = ""

    inner class DateViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val dateTextView: TextView

        init {
            dateTextView = itemView.findViewById(R.id.date)
        }
    }
    inner class ContentViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val content: TextView
        val isComplete: ImageView

        init {
            content = itemView.findViewById(R.id.content)
            isComplete = itemView.findViewById(R.id.is_complete)

            isComplete.setOnClickListener {
                Log.d("logcat", "to-do click: ${toDoList[adapterPosition].id}")
                activity.updateToDoComplete(toDoList[adapterPosition].id)
            }
        }
    }

    // view holder 구분 by created
    override fun getItemViewType(position: Int): Int {
        val todo = toDoList[position]
        val tempDate = todo.created.split("T")[0]

        return if (previousDate == tempDate) {
            0
        } // create date 일치
        else {
            previousDate = tempDate
            1 // create date 불일치
        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): RecyclerView.ViewHolder {
        return when (viewType) {
            // created date 불일치
            1 -> {
                DateViewHolder(
                    inflater.inflate(R.layout.todo_date, parent, false)
                )
            }
            // created date 일치
            else -> {
                ContentViewHolder(
                    inflater.inflate(R.layout.todo_content, parent, false)
                )
            }
        }
    }

    override fun getItemCount(): Int {
        return toDoList.size
    }

    override fun onBindViewHolder(holder: RecyclerView.ViewHolder, position: Int) {
        val todo = toDoList[position]

        if (holder is DateViewHolder) {
            holder.dateTextView.text = todo.created.split("T")[0]
        }
        if (holder is ContentViewHolder) {
            holder.content.text = todo.content
            if (todo.isComplete) {
                holder.isComplete.setImageDrawable(
                    activity.resources.getDrawable(
                        R.drawable.btn_radio_check,
                        activity.theme
                    )
                )
            } else {
                holder.isComplete.setImageDrawable(
                    activity.resources.getDrawable(
                        R.drawable.btn_radio,
                        activity.theme
                    )
                )
            }
        }
    }
}