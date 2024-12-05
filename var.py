import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(10 * x)  # Быстро осциллирующая функция

x1 = np.linspace(0, 2 * np.pi, 50)   # Мало точек (50)
x2 = np.linspace(0, 2 * np.pi, 500)  # Достаточно точек (500)
x3 = np.linspace(0, 2 * np.pi, 5000) # Очень много точек (5000)

plt.figure(figsize=(12, 6))
plt.plot(x1, f(x1), label='50 точек', marker='o')
plt.plot(x2, f(x2), label='500 точек')
plt.plot(x3, f(x3), label='5000 точек', linestyle='--', alpha=0.7)
plt.title('Влияние количества точек на график')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
