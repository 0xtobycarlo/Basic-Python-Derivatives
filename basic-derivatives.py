from math import pow
# dx is the "step" between each x value
dx = 0.05


def f(x):

    # to calculate the y values of the function
    return pow(x, 3) + 2


# x values
f_array_x = [x for x in
             np.arrange(0, 4, dx)]
# y values
f_array_y = [f(x) for x in
             np.arrange(0, 4, dx)]
# derivative calculation
f_array_deriv = np.gradient(f_array_y, dx)
