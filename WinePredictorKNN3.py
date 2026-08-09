import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler

def MarvellousClassifier(DataPath):
    border = "-"*40

    #Step 1 : Load the Dataset from csv file
    print(border)
    print("Step 1 : Load the Dataset from csv file")
    print(border)

    df = pd.read_csv(DataPath)

    print(border)
    print("Some Enteries from Data set :")
    print(df.head())
    print(border)

    #Step 2 : Clean the Dataset
    print(border)
    print("Step 2 : Clean the Dataset")
    print(border)

    df.dropna(inplace = True)

    print("Shape of dataset",df.shape)
    print("Total Records :",df.shape[0])
    print("Total columns :",df.shape[1])

    print(border)

    #Step 3 : Seperate Independent and Dependent Variables 
    print(border)
    print("Step 3 : Seperate Independent and Dependent Variables")
    print(border)

    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("Shape of X :",X.shape)
    print("Shape of Y :",Y.shape)
        
    print(border)
    print("Input Columns :",X.columns.tolist())
    print("Output Columns : Class")
    
def main():
    MarvellousClassifier("WinePredictor.csv")


if __name__ == "__main__":
    main()