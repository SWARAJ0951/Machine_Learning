import pandas as pd
import joblib

def LoadModel(Filename):
    model = joblib.load(Filename)

    print("Model Loaded Successfully")

    print(model.feature_names_in_)

    return model

def PredictPassenger(model):
    print("Enter The Information")

    Pclass = int(input("Enter Pclass (1/2/3)"))
    Sex = int(input("Enter Sex : (0-Male /1-Fale)"))
    Age = float(input("Enter Age :"))
    sibsp = int(input("Enter Sibsp"))
    Parch = int(input("Enter Parch"))
    Fare = float(input("Enter Fare :"))
    Embarked = float(input("Enter Embarked :(1/2/3)"))

    passenger = pd.DataFrame([{
        "Pclass" : Pclass,
        "Age" : Age,
        "Sex" : Sex,
        "sibsp" : sibsp,
        "Parch" : Parch,
        "Fare" : Fare,
        "Embarked_1.0" : 1 if Embarked ==1 else 0,
        "Embarked_2.0" : 1 if Embarked ==2 else 0,

    }]) 

    passenger = passenger[model.feature_names_in_]

    result = model.predict(passenger)

    print(result)
def main ():
    model = LoadModel("MarvellousTitanic.pkl")

    PredictPassenger(model)

if __name__ == "__main__":
    main()
