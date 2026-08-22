import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def main():
    #Step 1 : Load the Data
    df = pd.read_csv("Mall_Customers.csv")

    print("DataSet Laoded With values")
    print(df.head())

    print("Missing values ")
    print(df.isnull().sum())

    #Step 2 : Feature Selection
    X = df[["AnnualIncome","SpendingScore"]]
    print("Selected Features :")
    print(X.head())

    #Step 3 : Scale The data
    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    print("Scaled Data")
    print(X_scaled[:5])


if __name__ == "__main__":
    main()