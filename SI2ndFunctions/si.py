import matplotlib.pyplot as plt
import numpy as np
import datetime as dt

def secondOrderEqua(m, omega):
    assert m > 0

    mu = np.sqrt(1 - m**2)

    if m > 1:
        (tau1, tau2) = ((m - mu) / omega, (m + mu) / omega)

        def s(t):
            return 1 + 1 / (tau1 + tau2) * (tau1 * np.exp(-t / tau1) - tau2 * np.exp(-t / tau2))

    elif m == 1:
        tau = 1 / omega

        def s(t):
            return 1 - (1 + t / tau) * np.exp(-t / tau)

    else:
        phi = np.arccos(m)

        def s(t):
            return 1 - (np.exp(-m * omega * t) / mu) * np.sin(omega * mu * t + phi)

    return s

if __name__ == "__main__":

    (m, omega) = (0.5, 2)
    (m1, omega1) = (0.2, 2)
    
    axiscfgdict = {"xmin":0, "xmax":10, "ymin":0, "ymax":1.75}

    # plotfunc 1
    X = np.arange(0, 10, 10**-2)
    Y = secondOrderEqua(m, omega)(X)
    plt.plot(X, Y)

    # plotfunc 2
    X = np.arange(0, 10, 10**-2)
    Y = secondOrderEqua(m1, omega1)(X)
    plt.plot(X, Y)

    # plot +/- 5% line
    nVals = len(X)
    plt.plot(X, [0.95] * nVals, color="red")
    plt.plot(X, [1.05] * nVals, color="red")

    # annotate
    plt.title("Réponse d'un système du deuxième ordre (m, w) = ({}; {} puls.s^-1)".format(m, omega))
    plt.ylabel("s(t) / K.A")
    plt.xlabel("temps (sec)")

    # axis & grid config
    plt.axis(**axiscfgdict)
    plt.grid(True)

    #out
    plt.savefig(dt.datetime.now().strftime("%d-%m-%Y %H-%M-%S") + "mo-{}-{}.png".format(m, omega))
    plt.show()
