import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score

def MarvellousRegression(Datapath):
    border = "-"*40
    #Step 1 : Load The Data
    print(border)
    print("Step 1 : Load The Data")
    print(border)

    df = pd.read_csv(Datapath)

    print(df.head())

def main():
     MarvellousRegression("Advertising.csv")

if __name__ =="__main__":
    main()
