"""
loader.py — Reads the raw CSV from disk and returns a validated DataFrame.
All other modules receive data through this interface.
"""

import pandas as pd

from mlproj_cpp_py.data.schema import REQUIRED_COLUMNS


def load_csv(path: str) -> pd.DataFrame:
    """Load a CSV file and verify it contains the required columns.

    Args:
        path: Filesystem path to the CSV file.

    Returns:
        A pandas DataFrame with at least the required columns present.

    Raises:
        FileNotFoundError: If the path does not exist.
        ValueError: If required columns are missing.
    """
    # TODO: read the CSV into a DataFrame
    # TODO: check that all REQUIRED_COLUMNS are present; raise ValueError if not
    # TODO: return the validated DataFrame
    raise NotImplementedError
