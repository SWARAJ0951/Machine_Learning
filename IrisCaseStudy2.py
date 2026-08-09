from sklearn.datasets import load_iris

def main():
    print("-"*30)
    print("Iris Classfication Case Study ")
    print("-"*30)

    Dataset = load_iris()
    #METADATA OF THE DATASET
    print("Independent variables are:")
    print(Dataset.feature_names)
    
    print("Dependent variables are:")
    print(Dataset.target_names)

if __name__ == "__main__":
    main()