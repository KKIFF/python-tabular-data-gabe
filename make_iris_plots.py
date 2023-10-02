import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
def I_set():
    """A function that will make a scatterplot and do a linear regression for
    the petal length and sepal length of Iris setosa"""
    dataframe = pd.read_csv("iris.csv")
    setosa = dataframe[dataframe.species == "Iris_setosa"]
    x = setosa.petal_length_cm
    y = setosa.sepal_length_cm
    regression = stats.linregress(x,y)
    slope = regression.slope
    intercept = regression.intercept
    plt.scatter(x, y, label = 'Data')
    plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
    plt.xlabel("Petal length (cm)")
    plt.ylabel("Sepal length (cm)")
    plt.legend()
    plt.savefig("petal_v_sepal_length_regress_setosa.png")
    return "petal_v_sepal_length_regress_setosa.png"
def I_ver():
    """A function that will make a scatterplot and do a linear regression for
    the petal length and sepal length of Iris versicolor"""
    dataframe = pd.read_csv("iris.csv")
    versicolor = dataframe[dataframe.species == "Iris_versicolor"]
    x = versicolor.petal_length_cm
    y = versicolor.sepal_length_cm
    regression = stats.linregress(x,y)
    slope = regression.slope
    intercept = regression.intercept
    plt.scatter(x, y, label = 'Data')
    plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
    plt.xlabel("Petal length (cm)")
    plt.ylabel("Sepal length (cm)")
    plt.legend()
    plt.savefig("petal_v_sepal_length_regress_versicolor.png")
    return "petal_v_sepal_length_regress_versicolor.png"
def I_vir():
    """A function that will make a scatterplot and do a linear regression for
    the petal length and sepal length of Iris virginica"""
    dataframe = pd.read_csv("iris.csv")
    virginica = dataframe[dataframe.species == "Iris_virginica"]
    x = virginica.petal_length_cm
    y = virginica.sepal_length_cm
    regression = stats.linregress(x,y)
    slope = regression.slope
    intercept = regression.intercept
    plt.scatter(x, y, label = 'Data')
    plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
    plt.xlabel("Petal length (cm)")
    plt.ylabel("Sepal length (cm)")
    plt.legend()
    plt.savefig("petal_v_sepal_length_regress_virginica.png")
    return "petal_v_sepal_length_regress_virginica.png"

if __name__ == '__main__':
    I_set()
    I_ver()
    I_vir()
