import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import seaborn as sns

Border = "-"*30

############################
#Step1 : Load The DataSet
###########################

print(Border)
print("Step 1 : Load the dataset")
print(Border)

DataPath = "iris.csv"

df = pd.read_csv(DataPath)

print("DataSet Loaded Successfully")
print("Intial entries from dataset are :")
print(df.head())

############################
#Step2 : Data Analysis (EDA)
############################

print(Border)
print("Step 2 : Data Analysis (EDA)")
print(Border)

print("Shape of DataSet:",df.shape)

print("Column names :",list(df.columns))

print("Mising Values per column :")
print(df.isnull(). sum())

print("Class Distribution (Species Count)")
print(df["species"].value_counts())

print("Statistical Report of Dataset :")
print(df.describe())

####################################################
#Step3 : Decide Independent and Dependent Variables
####################################################

print(Border)
print("Step3 : Decide Independent and Dependent Variables")
print(Border)

#X : Independent Variables /Features
#Y : Dependent Variables /Labels

feature_cols = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)",
    ]

X = df[feature_cols]

Y = df["species"]

print("X Shape :",X.shape)
print("Y Shape :",Y.shape)

###########################################
#Step4: Visualisation Of DataSet
##########################################

print(Border)
print("Step4: Visualisation Of DataSet")
print(Border)

#SCATTER PLOT
plt.figure(figsize=(7,5))

for sp in df ["species"].unique():
    temp = df[df["species"]== sp]
    plt.scatter(temp["petal length (cm)"],temp["petal width (cm)"],label = sp)

plt.title("Marvellous Iris Case Study")

plt.xlabel("petal length (cm)")
plt.ylabel("petal width (cm)")

plt.legend()
plt.grid()
plt.show()

###########################################
#Step5: Split the DataSet For Training and Testing
##########################################

print(Border)
print("Step5: Split the DataSet For Training and Testing")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

print("Dataset spliting activity done ")

print("X :",X.shape)    #(150,4)
print("Y :",Y.shape)   #(150,)

print("X_train :",X_train.shape)   #(75,4)
print("X_test :",X_test.shape)    #(75,)

print("Y_train :",Y_train.shape)  #(75,)
print("Y_test :",Y_test.shape)   #(75,)

###########################################
#Step6: Build The Model
##########################################

print(Border)
print("Step6: Build The Model")
print(Border)

model = DecisionTreeClassifier(max_depth=5)

print("Model gets created succesfully")

###########################################
#Step7: Train The Model
##########################################

print(Border)
print("Step7: Train The Model")
print(Border)

model.fit(X_train,Y_train)

print("Model Trained Succesfully")

###########################################
#Step8: Test The Model
##########################################

print(Border)
print("Step8: Test The Model")
print(Border)

Y_pred = model.predict(X_test)

print("Model Testing Done")
print("Expected answers :")
print(Y_test)

print("Predicted Answers :")
print(Y_pred)