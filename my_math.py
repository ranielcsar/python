# import matplotlib.pyplot as plt


def _sum(a, b):
    return a + b


def _sub(a, b):
    return a - b


def _mult(a, b):
    return a * b


def _div(a, b):
    return a / b


# LINEAR REGRESSION
'''
Y = b0 + b1 * X

Y  =  Predicted output
X  =  Input feature or feature matrix in multiple linear regression
b0 =  Intercept (where the line crosses the Y-axis)
b1 =  Slope or coefficient that determines the line's steepness
'''

'''
Y = b0 + b1 * X

Y  =  Resultado esperado
X  =  Matriz de dados
b0 =  Interceptor (ponto onde a linha cruza o eixo Y)
b1 =  Inclinação ou coeficiente que determina a inclinação da linha
'''


def _linearRegression():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    # média
    x_average = sum(x) / len(x)
    y_average = sum(y) / len(y)

    # inclinação (b1)
    slope = (y_average - x_average) / (x_average)

    # interceptor (b0)
    intercept = y_average - slope * x_average

    print(slope, intercept)

    plt.scatter(x, y)
    plt.plot([x_average for x_average in range(1, 6)], [
             intercept + slope * x_average for x_average in range(1, 6)])
    plt.show()

    return slope, intercept
