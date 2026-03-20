"""
metrics.py — Computes and prints standard classification metrics.
Called after prediction to evaluate model quality on the test set.
"""

import pandas as pd


def evaluate(y_true: pd.Series, y_pred: pd.Series, y_prob: pd.Series) -> dict:
    """Compute classification metrics and return them as a dictionary.

    Args:
        y_true: Ground-truth churn labels (0 or 1).
        y_pred: Predicted binary labels from the model.
        y_prob: Predicted churn probabilities (used for ROC-AUC).

    Returns:
        Dict with keys: accuracy, precision, recall, f1, roc_auc.
    """
    # TODO: compute accuracy, precision, recall, f1 using sklearn.metrics
    # TODO: compute roc_auc_score from y_true and y_prob
    # TODO: return results as a dict
    raise NotImplementedError


def print_report(metrics: dict) -> None:
    """Print a formatted summary of the evaluation metrics.

    Args:
        metrics: Dict returned by evaluate().
    """
    # TODO: print each metric name and value in a readable format
    raise NotImplementedError
