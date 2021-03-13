import matplotlib.pyplot as plt
import numpy as np

def quad(x):
    lista = []
    for i in x:
        lista.append(1/i)
    return lista

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

plt.bar(x, quad(x))
plt.plot(x, quad(x), color='red')

plt.show()

y = filter(lambda n: n % 2 == 0, x)
for i in y:
    print(i)