import numpy as np
import pandas as pd 
import joblib 

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

#Step 1 : Load Data

#--------------------------------------------------------------
#.   Function Name : Load The Data
#    Description : Load the data from CSV
#    Input : Name of CSV file
#    Output : DataFrame
#    Author : Swaraj Jagtap
#    Date :16/08/2026
#---------------------------------------------------------------

def LoadData(filename):
    df = pd.read_csv(filename)

    print("Dataset Loaded Successfully")
    print(df.head())

    return df

#Step 2 : Data Preprocessing
#--------------------------------------------------------------
#.   Function Name : Preprocess Data
#    Description : It Process Data analysis
#    Input : Dataframe
#    Output : Updated DataFrame
#    Author : Swaraj Jagtap
#    Date :16/08/2026
#---------------------------------------------------------------

def Preprocess(df):
    df = df.drop(columns =[
        "Passengerid",
        "zero",
        "name"
        ],
        errors= "ignore"
    )
    #Handle Missing values 
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Fare"] = df["Fare"].fillna(df["Fare"].median())
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

   
    #Convert Categorical to Numeric data
    df = pd.get_dummies(
        df,
        columns=["Embarked"],
        drop_first= True,
        dtype= int
    )

    print(df.head())
    print("DataPreprocessing Completed")
    
    return df


#--------------------------------------------------------------
#.   Function Name : Main
#    Description : Entry Point Function
#    Input : NONE
#    Output : None
#    Author : Swaraj Jagtap
#    Date :16/08/2026
#---------------------------------------------------------------


def main():
    #Step 1 
    df = LoadData("MarvellousTitanicDataset.csv")

    #Step 2
    df = Preprocess(df)
if __name__ == "__main__":
    main()