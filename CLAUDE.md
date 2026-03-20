# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**mlproj-cpp-py** is a hybrid C++/Python project for customer churn prediction from tabular data.
Python owns the full ML pipeline. C++ provides a performance-critical normalizer module callable from Python via ctypes.

## Build Commands

### Python — install package in editable mode (run once)
```bash
pip install -e ".[dev]"
```

### C++
```bash
cd cpp && mkdir -p build && cd build && cmake .. && cmake --build .
```
Produces two targets: `mlproj` (executable) and `normalizer` (shared library for Python).

### Run the training pipeline
```bash
python scripts/train.py --data data/sample/churn_sample.csv
```

## Testing

```bash
# Run all Python tests
pytest tests/python/

# Run a single test file
pytest tests/python/test_loader.py
```

## Architecture

```
mlproj_cpp_py/              # Python package (import as: from mlproj_cpp_py.data import loader)
  data/
    schema.py               # Column definitions, feature lists, target column constant
    loader.py               # load_csv() — reads and validates the raw CSV
  preprocessing/
    pipeline.py             # build_preprocessor() — returns sklearn ColumnTransformer
  training/
    trainer.py              # build_pipeline(), train(), save_model()
  evaluation/
    metrics.py              # evaluate(), print_report()
  reporting/
    predictions.py          # save_predictions() — writes outputs/predictions.csv

scripts/
  train.py                  # CLI entry point — wires all modules together end-to-end

cpp/
  include/normalizer.h      # Public C API for the normalizer shared library
  src/normalizer.cpp        # TODO: min-max normalization implementation
  src/main.cpp              # Standalone C++ executable (smoke test for the C++ build)
  CMakeLists.txt            # Builds both mlproj executable and normalizer shared lib

data/
  sample/churn_sample.csv   # 50-row synthetic dataset for local development and tests

tests/python/               # pytest test stubs — one file per module
```

## Naming Conventions

- Python package and imports: `mlproj_cpp_py` (underscores)
- Repo/folder/PyPI name: `mlproj-cpp-py` (dashes)

## C++/Python Integration

`normalizer` is built as a shared library (`libnormalizer.so` / `normalizer.dll`).
Python loads it with `ctypes.CDLL` and calls `minmax_normalize(ptr, n)` directly.
No third-party binding library is needed for v0.1.
