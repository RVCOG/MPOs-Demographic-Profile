# indicators/utils.py
import pandas as pd
import numpy as np



def validate_columns(df, required_columns):
    missing = [
        col for col in required_columns if col not in df.columns
    ]
    if missing:
        raise ValueError(f"Missing columns: {missing}")


def safe_percent(numerator, denominator):
    return np.where(
        denominator > 0,
        numerator / denominator * 100,
        np.nan
    )