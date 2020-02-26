from sklearn.base import TransformerMixin
import pandas as pd
import numpy as np
class DataFrameEncoder(TransformerMixin):

    def __init__(self):
        """Finding the dummy values of the columns in DataFrame.

        Columns of dtype object are taken in array.

        The columns collectively taken and finding it's dummies, dropped first column and concated.

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
