import random
import matplotlib.pyplot as plt
import math
import numpy as np

print("1. Let's form the sample of random variable.")
n = raw_input('Input an amount of elements in sample (n): \n')
n = int(n)
if n < 0:
    print("n must be a natural number!")
    exit()

a = 1
b = 6
sample1 = []

for _ in range(n):
    e = random.uniform(0, 1)
    x1 = e * (b - a) + a
    x = round(x1, 4)
    #y = x
    y = 1/(x**2)
    sample1.append(y)

print("2. The sample of random variable is: \n")
print(sample1)


def quick_sort(array):
    return quick_sort([x for x in array[1:] if x < array[0]]) + [array[0]] + \
           quick_sort([x for x in array[1:] if x >= array[0]]) if len(array) > 1 else array

sort_sample = quick_sort(sample1)

print("")
print("3. Empirical series is: \n")
print(sort_sample)

if len(sort_sample) <= 100:
        m = int(math.sqrt(len(sort_sample)))
else:
        m = math.trunc(2 * math.log1p(len(sort_sample)))


def hist_eq_prob(sample):
    v = math.trunc(len(sample)//m)
    h = [sample[i*v-1]-sample[(i-1)*v] for i in xrange(1, m+1)]
    y = [sample[i*v] for i in xrange(m)] + [sample[-1]]
    P_y = map(lambda x: v/(len(sample)*x), h)
    if len(sample)%m != 0:
        h.append(sample[-1]-sample[v*m])
        P_y.append((len(sample)%m)/len(sample)/h[-1])

    _y = np.arange(0, 1, 0.0001)
    f_y = []
    for y0 in _y:
        for i in xrange(len(y)):
            if y[i] > y0:
                if i == 0:
                    f_y.append(0)
                    break
                else:
                    f_y.append(P_y[i-1])
                    break

            elif i == len(y)-1:
                f_y.append(0)
                break

    plt.fill(_y, f_y, color='#7EC0EE', alpha=0.5)
    plt.title("Equal Probability Histogram")
    plt.xlabel("x")
    plt.ylabel("f'(x)")
    plt.grid()
    plt.show()

if __name__ == "__main__":
    print("")
    print("4. Graphs of a function are:")
    hist_eq_prob(sort_sample)




