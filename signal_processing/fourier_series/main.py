import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 1000)
y = np.zeros_like(x)
terms = 30
for n in range(1, terms*2, 2):
    y += (4 / np.pi) * (1 / n) * np.sin(n * x)
    
plt.figure(figsize=(12,6))

plt.plot(
    x,
    y,
    linewidth=2,
    label=f"{terms} Harmonics"
)

plt.grid(True)

plt.title("Fourier Series - Square Wave")

plt.xlabel("x")

plt.ylabel("Amplitude")

plt.legend()

plt.savefig("output.png", dpi=300)

plt.show()