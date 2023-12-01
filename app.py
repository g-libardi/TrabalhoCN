from  numpy import linalg
import matplotlib.pyplot as plt

def linear_least_squares(x: list, y: list):
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x2 = sum([i**2 for i in x])
    sum_xy = sum([x[i]*y[i] for i in range(len(x))])
    n = len(x)
    a1 = (sum_x2 * sum_y - sum_x * sum_xy) / (n * sum_x2 - sum_x**2)
    a2 = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
    def f(x):
        return a1 + a2 * x
    return f, a1, a2

def draw_figure(x, y):
    f, a1, a2 = linear_least_squares(x, y)
    fig = plt.figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot()
    ax.scatter(x, y)
    ax.plot(x, [f(i) for i in x], color="red")
    
    # Set x-ticks
    x_ticks = plt.xticks()[0]
    new_ticks = x_ticks[::2]
    plt.xticks(new_ticks)
    
    return fig
