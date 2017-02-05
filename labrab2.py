from labrab1 import n, sort_sample
import matplotlib.pyplot as plt

import math

if n <= 100:
    M = math.trunc(math.sqrt(n))
else:
    M = math.trunc(2 * math.log1p(n))


def histograms_graphics():
    plt.title("Equal Interval Histogram")
    plt.xlabel("x")
    plt.ylabel("f'(x)")
    plt.hist(sort_sample, bins=M, normed=True, color='#7EC0EE', alpha=0.5)

    plt.grid()
    plt.show()


if __name__ == "__main__":
    print("")
    print("4. Graphs of a function are:")
    histograms_graphics()
