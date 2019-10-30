import pandas as pd
from sklearn.datasets import load_iris

def load_data():
    # Loading
    terror_df = pd.read_csv('Global_Terrorism.csv', encoding= "iso-8859-1")
    return terror_df

if __name__ == "__main__":
    load_data()