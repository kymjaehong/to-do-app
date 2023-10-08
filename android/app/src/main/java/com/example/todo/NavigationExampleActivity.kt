package com.example.todo

import androidx.navigation.fragment.findNavController
import com.example.todo.databinding.ActivityNavigationExampleBinding
import com.example.todo.ui.BaseActivity
import dagger.hilt.android.AndroidEntryPoint

@AndroidEntryPoint
class NavigationExampleActivity: BaseActivity() {

    override val binding by lazy {
        ActivityNavigationExampleBinding.inflate(layoutInflater)
    }

    private val navController = supportFragmentManager.findFragmentById(
        R.id.nav_host_example
    )?.findNavController()

    override fun onSupportNavigateUp(): Boolean {
        return navController?.navigateUp() ?: false
    }

}