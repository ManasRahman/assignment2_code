import pandas as pd
import numpy as np
from os import path, getcwd
from sklearn import model_selection
from typing import Tuple

def preprocess_online_shoppers() -> Tuple[pd.DataFrame, pd.DataFrame]:
    df : pd.DataFrame = pd.read_csv(path.join(path.dirname(__file__), 'online_shoppers_intention.csv'))
    df = df.reindex()
    # convert month to boolean columns
    df = pd.concat([df, pd.get_dummies(df.Month)], axis=1) \
           .drop(columns=['Month'])
    df = pd.concat([df, pd.get_dummies(df.VisitorType)], axis=1) \
           .drop(columns=['VisitorType'])
    df = pd.concat([df.drop(columns='Revenue'), df.Revenue], axis=1)
    df = df.reindex()
    
    df.to_csv(path.join(path.dirname(__file__), '../online_shoppers_processed.csv'))
    return df

if __name__ == "__main__":
    preprocess_online_shoppers()