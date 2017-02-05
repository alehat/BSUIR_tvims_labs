import random
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np

print("1. Let's form the sample of random variable.")
n = raw_input('Input an amount of elements in sample (n): \n')
n = int(n)
if n < 0:
    print("n must be a natural number!")
    exit()

a = 1
b = 6
sample = []

for _ in range(n):
    e = random.uniform(0, 1)
    x1 = e * (b - a) + a
    x = round(x1, 4)
    y = 1/(x**2)
    sample.append(y)

print("2. The sample of random variable is: \n")
print(sample)


def quick_sort(array):
    return quick_sort([x for x in array[1:] if x < array[0]]) + [array[0]] + \
           quick_sort([x for x in array[1:] if x >= array[0]]) if len(array) > 1 else array

sort_sample = quick_sort(sample)

print("")
print("3. Empirical series is: \n")
print(sort_sample)


def graph_emp():
    plt.title("Empirical Distribution Function")
    plt.xlabel("x")
    plt.ylabel("F'(x)")

    ecdf = sm.distributions.ECDF(sort_sample)
    x1 = [sort_sample[n-1], 6.2]
    y1 = [1, 1]
    plt.step(x1, y1, color='red')

    x2 = [-0.3, sort_sample[0]]
    y2 = [0.002, 0.002]
    plt.step(x2, y2, color='red')

    x2 = [sort_sample[0], sort_sample[0]]
    y2 = [0, ecdf(sort_sample[0])]
    plt.step(x2, y2, color='red')

    x3 = sort_sample
    y3 = ecdf(sort_sample)

    plt.plot(x3, y3, color='blue')

    x = np.linspace(min(sort_sample), max(sort_sample))
    y = ecdf(x)
    plt.axis([-0.3, 1.1, 0.0, 1.1])
    plt.step(x, y, color='red')
    plt.grid()
    plt.show()

    plt.hold(True)

if __name__ == "__main__":
    print("")
    print("4. Graph of a Empirical Distribution Function is:")
    graph_emp()







