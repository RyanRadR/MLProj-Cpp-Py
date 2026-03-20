"""
predictions.py — Saves model predictions for the test set to a CSV file.
Output columns: customer_id, churn_probability, predicted_label.
"""

import pandas as pd


def save_predictions(customer_ids: pd.Series, y_prob: pd.Series, y_pred: pd.Series, path: str) -> None:
    """Write predictions to a CSV file.

    Args:
        customer_ids: Series of customer ID values (one per test row).
        y_prob: Predicted churn probabilities.
        y_pred: Predicted binary labels.
        path: Output file path (e.g. "outputs/predictions.csv").
    """
    # TODO: assemble a DataFrame with columns: customer_id, churn_probability, predicted_label
    # TODO: write it to path with df.to_csv(path, index=False)
    raise NotImplementedError
