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

#--------------------------------------------------------------
#.   Function Name : Main
#    Description : Entry Point Function
#    Input : NONE
#    Output : None
#    Author : Swaraj Jagtap
#    Date :16/08/2026
#---------------------------------------------------------------


def main():
    LoadData("MarvellousTitanicDataset.csv")


if __name__ == "__main__":
    main()