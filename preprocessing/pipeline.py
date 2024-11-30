from preprocessing.nan_filling import CategoricalNanFiller, NumericalNanFiller
from preprocessing.utils import preprocessing_map
from tqdm import tqdm


class Pipe:
    def __init__(self: 'Pipe',
                 cat_cols: list[str],
                 num_cols: list[str],
                 ):
        self.cat_cols_set = set(cat_cols)
        self.num_cols_set = set(num_cols)
        self.cols = cat_cols + num_cols
        self.nan_fillers_dict = {}
        self.preproc_dict= {}


    def fit_transform(self:'Pipe', df):
        for col in tqdm(self.cols):
            if col in self.cat_cols_set:
                filler = CategoricalNanFiller()
            elif col in self.num_cols_set:
                filler = NumericalNanFiller()
            else:
                continue
            filler.fit(df[col])
            df[col] = filler.transform(df[col])
            preproc = preprocessing_map[col]
            preproc.fit(df[col])
            df[col] = preproc.transform(df[col])
            self.nan_fillers_dict[col] = filler
            self.preproc_dict[col] = preproc
        return df

    def transform(self: 'Pipe', df):
        for col in tqdm(self.cols):
            df[col] = self.nan_fillers_dict[col].transform(df[col])
            df[col] = self.preproc_dict[col].transform(df[col])
        return df





