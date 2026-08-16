import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousPredicter():
    # Step 1 : Load the Data
    X=[1,2,3,4,5]
    Y=[3,4,2,4,5]

    print("Values Of Independent variables X :",X)
    print("Values Of Dependent variables Y :",Y)

    sum_x = 0
    sum_y = 0

    for i in range(len(X)):
        sum_x = sum_x + X[i]
        sum_y = sum_y + Y[i]

    mean_X = sum_x / len(X)
    mean_Y = sum_y / len(Y)

    print("Mean_X is :",mean_X)
    print("Mean_Y is :",mean_Y)
    


def main():
    MarvellousPredicter()

if __name__ =="__main__":
    main()