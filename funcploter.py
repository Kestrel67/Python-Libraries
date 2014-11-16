import matplotlib.pyplot as plt
import numpy as np

# func : function lambda float --> float
# xlimits : xmin, xmax
# accuracy gap = 10**-prec
# ylimites : ymin, ymax
# save : file location
# display : show figure
def graph(func, xmin = -1, xmax = 1, prec = 2, save = False, display = True, title = None, **kargs):
    X = np.arange(xmin, xmax, 10**-prec)

    plt.plot(X, [func(x) for x in X])

    plt.axis(xmin=xmin, xmax=xmax)

    if 'ymin' in kargs:
        plt.axis(ymin=kargs['ymin'])

    if 'ymax' in kargs:
        plt.axis(ymax=kargs['ymax'])

    plt.grid(True)

    if title:
        plt.title(title)

    # save figure
    if save:
        print('figure saved at {}'.format(save))
        plt.savefig(save)

    # show figure
    if display:
        plt.show()
    else:
        print('figure not showed')

if __name__ == '__main__':
    graph(lambda x: x**-2 - 3*x * np.cos(x), -10, 10, ymin = -30, ymax = 30, save = 'examplegraph.png', display = False, title = "f(x) = x**-2 - 3*x * cos(x)")
