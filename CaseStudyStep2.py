import pandas as pd

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




