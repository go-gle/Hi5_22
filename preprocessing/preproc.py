import pandas as pd
import numpy as np


class Clipper:
    def __init__(self, trim: bool = True, perc: float = 0.005):
        self.trim = trim
        self.perc = perc
        self.upper_limit, self.lower_limit = None, None

    def fit(self: 'Clipper', col: pd.Series) -> np.ndarray:
        self.upper_limit = col.quantile(1 - self.perc)
        self.lower_limit = col.quantile(self.perc)

    def transform(self: 'Clipper', col: pd.Series) -> np.ndarray:
        transformed_col = np.where(col >= self.upper_limit, self.upper_limit, col)
        transformed_col = np.where(col <= self.lower_limit, self.lower_limit, transformed_col)
        return transformed_col


class Identity:
    def __init__(self):
        pass

    def fit(self: 'Identity', col: pd.Series) -> np.ndarray:
        return self

    def transform(self: 'Identity', col: pd.Series) -> np.ndarray:
        return col
