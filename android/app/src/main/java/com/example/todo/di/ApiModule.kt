package com.example.todo.di

import com.example.todo.data.api.ToDoRetrofit
import com.skydoves.sandwich.adapters.ApiResponseCallAdapterFactory
import dagger.Module
import dagger.Provides
import dagger.hilt.InstallIn
import dagger.hilt.components.SingletonComponent
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import javax.inject.Singleton


@InstallIn(SingletonComponent::class)
@Module
object ApiModule {
    private const val currVersion = "v1/"
    private const val baseUrl = "http://10.0.2.2:8000/api/$currVersion"

    @Singleton
    @Provides
    fun provideRetrofit(): Retrofit =
        Retrofit
            .Builder()
            .baseUrl(baseUrl)
            .addCallAdapterFactory(ApiResponseCallAdapterFactory.create()) // sandwich
            .addConverterFactory(GsonConverterFactory.create())
            .build()

    @Singleton
    @Provides
    fun provideToDoService(retrofit: Retrofit): ToDoRetrofit {
        return retrofit.create(ToDoRetrofit::class.java)
    }
}