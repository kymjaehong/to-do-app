package com.example.todo.presentation_layer.ui

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.viewbinding.ViewBinding

abstract class BaseFragment<fragmentViewBinding: ViewBinding>: Fragment() {
    private var _binding: fragmentViewBinding? = null

    protected val binding: fragmentViewBinding
        get() = _binding!!

    abstract fun getViewBinding(): fragmentViewBinding

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        return getViewBinding().also { _binding = it }.root
    }

    override fun onDestroyView() {
        _binding = null
        super.onDestroyView()
    }
}