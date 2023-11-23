package com.example.todo.di

import android.content.Context
import androidx.room.Room
import dagger.Module
import dagger.Provides
import dagger.hilt.InstallIn
import dagger.hilt.android.qualifiers.ApplicationContext
import dagger.hilt.components.SingletonComponent
import javax.inject.Singleton

@Module
@InstallIn(SingletonComponent::class)
object LocalModule {

//    @Singleton
//    @Provides
//    fun provideBlogDb(@ApplicationContext context: Context): ToDoDatabase {
//        return Room.databaseBuilder(
//            context,
//            ToDoDatabase::class.java,
//            ToDoDatabase.DATABASE_NAME
//        )
//            .fallbackToDestructiveMigration()
//            .build()
//    }
//
//    @Singleton
//    @Provides
//    fun provideBlogDao(toDoDatabase: ToDoDatabase): ToDoDao {
//        return ToDoDatabase.toDoDao()
//    }
}