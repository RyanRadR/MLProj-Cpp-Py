"""
schema.py — Defines the expected columns and types for the churn dataset.
Used by the loader to validate input CSVs before any processing.
"""

# Columns that must be present in the raw CSV
REQUIRED_COLUMNS: list[str] = [
    "customer_id",
    "age",
    "tenure_months",
    "monthly_charges",
    "contract_type",
    "internet_service",
    "num_support_tickets",
    "paperless_billing",
    "payment_method",
    "churn",  # target label: 0 or 1
]

# Numeric feature columns (will be scaled)
NUMERIC_FEATURES: list[str] = [
    "age",
    "tenure_months",
    "monthly_charges",
    "num_support_tickets",
]

# Categorical feature columns (will be one-hot encoded)
CATEGORICAL_FEATURES: list[str] = [
    "contract_type",
    "internet_service",
    "paperless_billing",
    "payment_method",
]

# Column used to identify rows but not used in training
ID_COLUMN: str = "customer_id"

# Target column the model predicts
TARGET_COLUMN: str = "churn"
