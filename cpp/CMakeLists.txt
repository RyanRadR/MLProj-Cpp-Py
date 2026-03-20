cmake_minimum_required(VERSION 3.16)
project(mlproj_cpp_py LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(mlproj
    src/main.cpp
)

target_include_directories(mlproj_cpp_py PRIVATE includes)
