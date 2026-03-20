"""
train.py — CLI entry point for the training pipeline.
Wires together: load → preprocess → train → evaluate → save predictions.

Usage:
    python scripts/train.py --data data/sample/churn_sample.csv
"""

import argparse  # Standard library argument parser for the CLI


def parse_args() -> argparse.Namespace:
    """Define and parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Train the churn prediction model.")
    # --data: path to the input CSV file
    parser.add_argument("--data", required=True, help="Path to the input CSV file.")
    # --output: where to write the predictions CSV
    parser.add_argument("--output", default="outputs/predictions.csv", help="Path for predictions output.")
    # --model-out: where to save the serialized model
    parser.add_argument("--model-out", default="outputs/model.joblib", help="Path to save the trained model.")
    return parser.parse_args()


def main() -> None:
    """Run the full training and evaluation pipeline."""
    args = parse_args()

    # Step 1: Load data from CSV using the loader module
    # TODO: call mlproj_cpp_py.data.loader.load_csv(args.data)

    # Step 2: Split into train/test sets
    # TODO: use sklearn train_test_split; keep customer_id separate

    # Step 3: Build the preprocessor and full training pipeline
    # TODO: call build_preprocessor() then build_pipeline()

    # Step 4: Fit the pipeline on training data
    # TODO: call train(pipeline, X_train, y_train)

    # Step 5: Generate predictions on the test set
    # TODO: pipeline.predict and pipeline.predict_proba

    # Step 6: Evaluate and print metrics
    # TODO: call evaluate() then print_report()

    # Step 7: Save predictions to disk
    # TODO: call save_predictions()

    # Step 8: Save model to disk
    # TODO: call save_model()


if __name__ == "__main__":
    main()
