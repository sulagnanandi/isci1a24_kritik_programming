import numpy as np
import matplotlib.pyplot as plt


def f1(x): #part A function
    return x ** 2


def f2(x): #part B function
    return x ** 4 - 2 * x ** 2


def f3(x): #part C
    if x > 0:
        return x ** x
    elif x == 0:
        return 1
    else:
        return abs(x) ** abs(x)

def f4(x): return abs(x)

def dydx(f, x):
    return (f(x + 10 ** -10) - f(x - 10 ** -10)) / (2 * 10 ** -10)


def find_minimum(f, x0, learning_rate):
    x_coords = [x0]
    y_coords = [f(x0)]

    i = 1

    while abs(dydx(f, x_coords[i-1])) > 10 ** -10:

        x_coords.append(x_coords[i-1] - learning_rate * dydx(f, x_coords[i-1]))
        y_coords.append(f(x_coords[i]))
        print(dydx(f, x_coords[i - 1]))
        print(x_coords[i], y_coords[i])
        i += 1

        if i == 10 ** 3:
            return "Error! No minimum could be found. Try a different learning rate."

    # Plotting portion. You may adjust as you please.
    plot_range = np.linspace(min(x_coords) - 0.5, max(x_coords) + 0.5, 10000)  # a nice plot range
    # to make look good
    function_range = [f(i) for i in plot_range]
    plt.plot(plot_range, function_range)  # this plots the function f(x)
    plt.plot(x_coords, y_coords)  # This will plot the
    # sequence of points x_n, f(x_n)
    return "Minimum of this function is at (" + str(round(x_coords[i - 1], 3)) + ", " + str(round(y_coords[i - 1], 3)) + ")."
    # last x_n and y_n, #rounded to three decimal places.

# controls user input, allows user to find different roots by trying different x0's and learning rates
def main():
    done = False

    while not done:
        function_name = (input("Enter a which function you want to minimize (1, 2, 3, 4): "))

        function = None

        if function_name == "1":
            function = f1
        elif function_name == "2":
            function = f2
        elif function_name == "3":
            function = f3
        elif function_name == "4":
            function = f4
        x0 = float(input("Enter a starting point for the optimization: "))
        learning_rate = float(input("Enter a learning rate for the optimization: "))

        print(find_minimum(function, x0, learning_rate))
        continue_or_not = input("Would you like to continue (yes or no): ")

        if continue_or_not.lower() == "no":
            done = True


main()
