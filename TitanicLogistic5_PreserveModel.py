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

#Step 3 : Split DataSet
#--------------------------------------------------------------
#.   Function Name : Preprocess Data
#    Description : It Process Data analysis
#    Input : Dataframe
#    Output : Updated DataFrame
#    Author : Swaraj Jagtap
#    Date :16/08/2026
#---------------------------------------------------------------
def SplitData(df):
    X = df.drop("Survived",axis=1)
    Y = df["Survived"]

    X_train , X_test , Y_train , Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,  
        random_state=42

    )
    print("Data Spliting Completed Successfully")
    return X_train , X_test , Y_train , Y_test

#Step 4 : Train Model
#--------------------------------------------------------------
#.   Function Name : Train Model
#    Description : It Performs Model Training
#    Input : Training Features and labels
#    Output : Trained Model
#    Author : Swaraj Jagtap
#    Date :16/08/2026
#---------------------------------------------------------------
def Trainmodel(X_train,Y_train):
    model = LogisticRegression(max_iter=1000)

    model = model.fit(X_train,Y_train)

    print("Model Tarined Successfully")

    return model

#Step 5 : Evaluate Model
#--------------------------------------------------------------
#.   Function Name : Evaluate Model
#    Description : It Performs Model Testing
#    Input : model,testing data(Features and Labels)
#    Output : None
#    Author : Swaraj Jagtap
#    Date :16/08/2026
#---------------------------------------------------------------
def EvaluteModel(model,X_test,Y_test):
    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test,Y_pred)
    print("Accuracy is :",accuracy)

    print(confusion_matrix(Y_test,Y_pred))

#Step 6 : Preserve Model
#--------------------------------------------------------------
#.   Function Name : Preserve Model
#    Description : It Performs Model Preservation into .pkl file
#    Input : model
#    Output : None
#    Author : Swaraj Jagtap
#    Date :16/08/2026
#---------------------------------------------------------------
def PreserveModel(model,filename):
    joblib.dump(model,filename)

    print("Model Preserved with name :",filename)
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

    #Step 3 
    X_train , X_test , Y_train , Y_test = SplitData(df)

    #Step 4 
    model = Trainmodel(X_train,Y_train)

    #Step 5 
    EvaluteModel(model,X_test,Y_test)

    #Step 6
    PreserveModel(model,"Marvellous Titanic.pkl")

if __name__ == "__main__":
    main()