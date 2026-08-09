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



