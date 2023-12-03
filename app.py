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

def draw_figure(x, y, x_label="1/sqrt(M)", y_label="1/Tk"):
    x = x.copy()
    y = y.copy()
    f, a1, a2 = linear_least_squares(x, y)
    fig = plt.figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot()

    # Move left y-axis to centre, passing through (0,0)
    ax.spines['left'].set_position('zero')

    # Keep bottom x-axis at the bottom, making it always visible
    # No need to change its position

    # Eliminate upper and right axes
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # Show ticks in the left and lower axes only
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    ax.scatter(x, y)
    x.insert(0, 0)
    ax.plot(x, [f(i) for i in x], color="red")
    ax.scatter(0, a1, color="green")
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    # Set y-limits
    y_min, y_max = ax.get_ylim()
    ax.set_ylim(y_min - 0.1 * (y_max - y_min), y_max + 0.1 * (y_max - y_min))

    # Rest of the code
    x_ticks = plt.xticks()[0]
    new_ticks = x_ticks[::2]
    plt.xticks(new_ticks)

    return fig
