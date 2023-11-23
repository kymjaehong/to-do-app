package com.example.todo.di

import com.example.todo.data.api.ToDoRetrofit
import com.example.todo.data.room.ToDoDao
import com.example.todo.presentation.repository.ToDoRepository
import dagger.Module
import dagger.Provides
import dagger.hilt.InstallIn
import dagger.hilt.components.SingletonComponent
import javax.inject.Singleton

@Module
@InstallIn(SingletonComponent::class)
object RepositoryModule {

    @Singleton
    @Provides
    fun provideToDoRepository(
        //toDoDao: ToDoDao,
        toDoRetrofit: ToDoRetrofit
    ): ToDoRepository {
        return ToDoRepository(
            //toDoDao,
            toDoRetrofit
        )
    }
}