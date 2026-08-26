import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report


#----------------------------------------
#Step 1 : Load The dataset
#----------------------------------------

df = pd.read_csv("breast_cancer.csv")

print("Shape Of dataset",df.shape)
print("First 5 Records",df.head())

#----------------------------------------
#Step 2 : Separate Features and Labels 
#----------------------------------------

X = df.drop("target", axis=1)

Y = df["target"]

print("X Shape",X.shape)
print("Y Shape",Y.shape)

#--------------------------------------------------
#Step 3 : Split dataset for training and testing 
#-------------------------------------------------

X_train , X_test , Y_train , Y_test = train_test_split(
                                                X,
                                                Y,
                                                test_size=0.2,
                                                random_state=42
                                                )

#--------------------------------------------------
#Step 4 : Scale the Features
#-------------------------------------------------

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)

#--------------------------------------------------
#Step 5.1 : Create The Base Model
#-------------------------------------------------

base_model = DecisionTreeClassifier(random_state=42)

#--------------------------------------------------
#Step 5.2 : Create The Bagging Model
#-------------------------------------------------

model = BaggingClassifier(
    estimator=base_model,
    n_estimators=10,
    random_state=42

    )

#--------------------------------------------------
#Step 6 : Train The Model
#-------------------------------------------------

model = model.fit(X_train,Y_train)

#--------------------------------------------------
#Step 7 : Test The Model
#-------------------------------------------------

Y_pred = model.predict(X_test)

#--------------------------------------------------
#Step 8 : Evaluate The Model
#-------------------------------------------------

print("Accuracy :",accuracy_score(Y_test,Y_pred))
print("Confusion Matrix :",confusion_matrix(Y_test,Y_pred))

