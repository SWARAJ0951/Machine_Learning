import matplotlib.pyplot as plt

def main():
    language = ["C","C++","Java","Python"]
    students = [30,40,35,55]
 
    plt.bar(
        language,                 #value of x
        students,                 ##value of y
        width= 0.6,               #width of bar
        edgecolor = "black",      #border color of bar
        linewidth = 1,            #width of bar border
        alpha = 0.8,              #transparence 0 to 1
        label = "Students"        #legend text
    )

    plt.title("Marvellous Bar Plot")
    plt.xlabel("Languages")
    plt.ylabel("Number of Students")

    plt.legend()

    plt.show()



    
if __name__ == "__main__":
    main()