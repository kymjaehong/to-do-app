package com.example.todo.data_layer.di

import com.example.todo.api.ToDoRetrofit
import com.example.todo.data_layer.room.ToDoDao
import com.example.todo.presentation_layer.repository.ToDoRepository
import dagger.Module
import dagger.hilt.InstallIn
import dagger.hilt.components.SingletonComponent
import javax.inject.Singleton

@Module
@InstallIn(SingletonComponent::class)
internal abstract class RepositoryModule {

    @Singleton
    abstract fun provideToDoRepository(
        toDoDao: ToDoDao,
        toDoRetrofit: ToDoRetrofit
    ): ToDoRepository {
        return ToDoRepository(toDoDao, toDoRetrofit)
    }
}