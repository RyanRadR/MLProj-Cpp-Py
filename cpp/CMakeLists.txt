cmake_minimum_required(VERSION 3.16)
project(mlproj_cpp_py LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)          # Require C++17 features
set(CMAKE_CXX_STANDARD_REQUIRED ON) # Fail if compiler doesn't support C++17

# --- Executable target (development/debug entry point) ---
add_executable(mlproj
    src/main.cpp
)
target_include_directories(mlproj PRIVATE include)  # Expose include/ to the executable

# --- Shared library target (loaded by Python via ctypes) ---
add_library(normalizer SHARED
    src/normalizer.cpp              # Min-max normalization implementation
)
target_include_directories(normalizer PRIVATE include)  # Expose include/ to the library
