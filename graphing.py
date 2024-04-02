import numpy as np
from matplotlib import pyplot as plt


def plot_runtimes_test():
    # borrowed code from the following github repo:
    # https://gist.github.com/niftycode/917bb33be4e91a10b1fffd020f987f94
    # Stylesheets defined in Matplotlib

    # Set up runtime comparisons
    n = np.linspace(1, 6, 1000)
    labels = ['Constant', 'Logarithmic', 'Linear', 'Log Linear', 'Quadratic', 'Cubic', 'Exponential']
    big_o = [np.ones(n.shape), np.log(n), n, n * np.log(n), n ** 2, n ** 3, 2 ** n]

    # Plot setup
    plt.figure(figsize=(12, 10))
    plt.ylim(0, 50)

    for i in range(len(big_o)):
        plt.plot(n, big_o[i], label=labels[i])

    plt.legend(loc=0)
    plt.ylabel('Relative Runtime')
    plt.xlabel('Input Size')
    plt.savefig('big-o-notation.png')

    plt.show()