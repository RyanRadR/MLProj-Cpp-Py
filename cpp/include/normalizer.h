#pragma once  // Prevents this header from being included more than once

// C linkage so Python can call these functions via ctypes without name mangling
extern "C" {

    // Normalize an array of doubles in-place using min-max scaling to [0, 1]
    // data: pointer to the array
    // n:    number of elements
    void minmax_normalize(double* data, int n);

}  // extern "C"
