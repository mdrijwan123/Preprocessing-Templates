from sklearn.base import TransformerMixin
import pandas as pd
import numpy as np
class DataFrameEncoder(TransformerMixin):

    def __init__(self):
        """Impute missing values.

        Columns of dtype object are imputed with the most frequent value 
        in column.

        Columns of other types are imputed with mean of column.

        """
    def fit(self, X, y=None):
        self.object_col = []
        for col in X.columns:
            if(X[col].dtype == np.dtype('O')):
                self.object_col.append(col)
        return self

    def transform(self, X, y=None):
        dummy_df = pd.get_dummies(X[self.object_col],drop_first=True)
        X.drop(X[self.object_col],inplace=True,axis=1)
        X = pd.concat([dummy_df,X],axis=1)
        return X