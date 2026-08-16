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

    #Step 2 :Remove Unwanted Columns 
    print(border)
    print("Step 2 :Remove Unwanted Columns ")
    print(border)

    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    print(df.head())

    #Step 3 : Check Missing Values

    print(border)
    print("Step 3 : Check Missing Values")
    print(border)

    print("Total Missing Values :")
    print(border)
    print(df.isnull().sum())
    print(border)

    #Step 4 : Statistical Summary
    print(border)
    print("Step 4 : Statistical Summary")
    print(border)

    print(df.describe())

    #Step 5 : Correlation
    print(border)
    print("Step 5 : Correlation")
    print(border)

    print(df.corr())

    #Step 6 : Separate Independent and Dependent Variables
    print(border)
    print("Step 6 : Separate Independent and Dependent Variables")
    print(border)

    X = df[["TV","radio","newspaper"]]
    Y = df["sales"]

    print("Independent variables:" ,X.head())
    print("Dependent Variables :" ,Y.head())

    #Step 7 : Split the Dataset
    print(border)
    print("Step 7 : Split the data")
    print(border)

    X_train,X_test,Y_train,Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    print("Training Data :",X_train.shape)
    print("Testing Data :",X_test.shape)

    #Step 8 : Create and Train the Model
    print(border)
    print("Step 8 : Create and Train the Model")
    print(border)

    model = LinearRegression()

    model = model.fit(X_train,Y_train)
    print("Model Trained Successfully ")

    #Step 9 : Test The Model
    print(border)
    print("Step 9 : Test The Model")
    print(border)

    Y_pred = model.predict(X_test)

    print("Expected Answers :")
    print(Y_test[:3])

    print("Predicted Answers :")
    print(Y_pred[:3])
    
def main():
     MarvellousRegression("Advertising.csv")

if __name__ =="__main__":
    main()