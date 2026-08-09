import pandas as pd
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