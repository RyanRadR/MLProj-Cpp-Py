# Tests for mlproj_cpp_py.data.loader
import pytest
import pandas as pd
from mlproj_cpp_py.data.loader import load_csv


def test_load_csv_returns_dataframe():
    # TODO: call load_csv with data/sample/churn_sample.csv and assert isinstance result pd.DataFrame
    raise NotImplementedError


def test_load_csv_missing_column_raises():
    # TODO: create a temp CSV missing a required column and assert load_csv raises ValueError
    raise NotImplementedError


def test_load_csv_file_not_found():
    # TODO: assert load_csv raises FileNotFoundError for a nonexistent path
    raise NotImplementedError
