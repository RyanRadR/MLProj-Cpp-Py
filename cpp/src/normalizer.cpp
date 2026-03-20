#include "normalizer.h"  // Public API declaration

// TODO: implement minmax_normalize
// Steps:
//   1. Find the min and max values in data[0..n-1]
//   2. If max == min, set all values to 0.0 (avoid division by zero)
//   3. Otherwise, transform each element: data[i] = (data[i] - min) / (max - min)
extern "C" void minmax_normalize(double* data, int n)
{
    // TODO: implement
}
