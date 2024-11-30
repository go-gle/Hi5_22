import pandas as pd

class TimeFeaturesMonth:
    def __init__(self):
        pass

    def fit(self: 'TimeFeaturesMonth', col: pd.Series):
        return self

    def transform(self: 'TimeFeaturesMonth', col: pd.Series) -> pd.DataFrame:
        col = pd.to_datetime(col)
        df = pd.DataFrame()
        df['month'] = col.dt.month
        return df['month']
    
class TimeFeaturesYear:
    def __init__(self):
        pass

    def fit(self: 'TimeFeaturesYear', col: pd.Series):
        return self

    def transform(self: 'TimeFeaturesYear', col: pd.Series) -> pd.DataFrame:
        col = pd.to_datetime(col)
        df = pd.DataFrame()
        df['Year'] = col.dt.year
        return df['Year']
    
class TimeFeaturesWeek:
    def __init__(self):
        pass

    def fit(self: 'TimeFeaturesWeek', col: pd.Series):
        return self

    def transform(self: 'TimeFeaturesWeek', col: pd.Series) -> pd.Series:
        col = pd.to_datetime(col)
        df = pd.DataFrame()
        df['Week'] = col.dt.week
        return df['Week']
    
class TimeFeaturesSeason:
    def __init__(self):
        self.map = {1: 0, 2: 0, 3: 1, 4: 1, 5: 1, 6: 2, 7: 2, 8: 2, 9: 2, 10: 3, 11: 3, 12: 0}

    def fit(self: 'TimeFeaturesSeason', col: pd.Series):
        return self

    def transform(self: 'TimeFeaturesSeason', col: pd.Series) -> pd.Series:
        return col.apply(lambda x: self.map[x.month])
        
        