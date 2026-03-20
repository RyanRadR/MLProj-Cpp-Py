"""
pipeline.py — Assembles the sklearn preprocessing pipeline.
Combines numeric scaling and categorical encoding into one ColumnTransformer.
"""

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

from mlproj_cpp_py.data.schema import NUMERIC_FEATURES, CATEGORICAL_FEATURES


def build_preprocessor() -> ColumnTransformer:
    """Return a ColumnTransformer that scales numeric cols and encodes categoricals.

    Returns:
        An unfitted sklearn ColumnTransformer ready to be used in a Pipeline.
    """
    # TODO: build a numeric transformer (e.g. StandardScaler or MinMaxScaler)
    # TODO: build a categorical transformer (e.g. OneHotEncoder)
    # TODO: combine into a ColumnTransformer with NUMERIC_FEATURES and CATEGORICAL_FEATURES
    # TODO: return the ColumnTransformer
    raise NotImplementedError
