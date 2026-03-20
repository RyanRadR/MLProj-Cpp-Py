"""
trainer.py — Fits a model pipeline on training data and saves it to disk.
The full sklearn Pipeline (preprocessor + classifier) is trained here.
"""

import pandas as pd
from sklearn.pipeline import Pipeline


def build_pipeline(preprocessor) -> Pipeline:
    """Wrap the preprocessor and a classifier into a single sklearn Pipeline.

    Args:
        preprocessor: A fitted or unfitted ColumnTransformer from pipeline.py.

    Returns:
        An unfitted sklearn Pipeline ending in a classifier step.
    """
    # TODO: choose a baseline classifier (e.g. LogisticRegression)
    # TODO: return Pipeline([("preprocessor", preprocessor), ("classifier", clf)])
    raise NotImplementedError


def train(pipeline: Pipeline, X: pd.DataFrame, y: pd.Series) -> Pipeline:
    """Fit the pipeline on training data.

    Args:
        pipeline: Unfitted sklearn Pipeline from build_pipeline().
        X: Feature DataFrame (all columns except target).
        y: Target Series (churn labels).

    Returns:
        The fitted Pipeline.
    """
    # TODO: call pipeline.fit(X, y) and return the fitted pipeline
    raise NotImplementedError


def save_model(pipeline: Pipeline, path: str) -> None:
    """Serialize the fitted pipeline to disk with joblib.

    Args:
        pipeline: A fitted sklearn Pipeline.
        path: Output file path (e.g. "outputs/model.joblib").
    """
    # TODO: use joblib.dump to save pipeline to path
    raise NotImplementedError
