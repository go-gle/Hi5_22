import pandas as pd

class CategoricalNanFiller:
    def __init__(self, fill_value: str = 'missing'):
        self.fill_value = fill_value

    def fit(self: 'CategoricalNanFiller', col: pd.Series):
        return self
    
    def transform(self: 'CategoricalNanFiller', col: pd.Series) -> pd.Series:
        return col.fillna(self.fill_value)
    

class NumericalNanFiller:
    def __init__(self):
        self.mean = None

    def fit(self: 'NumericalNanFiller', col: pd.Series):
        self.mean = col.mean()
        return self
    
    def transform(self: 'NumericalNanFiller', col: pd.Series) -> pd.Series:
        return col.fillna(self.mean)
    

    