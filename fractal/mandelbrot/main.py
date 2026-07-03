import numpy as np
import matplotlib.pyplot as plt
# Image resolution
WIDTH = 1000
HEIGHT = 1000
# Complex plane boundaries
REAL_MIN = -2.0
REAL_MAX = 1.0

IMAG_MIN = -1.5
IMAG_MAX = 1.5
MAX_ITER = 100

def mandelbrot(c):
    """
    Return the number of iteration before the point escapes.
    """

    z=0
    for i in range(MAX_ITER):
        z=z*z+c

        if abs(z)>2:
            return i
    return MAX_ITER
    

image = np.zeros((HEIGHT, WIDTH))
for y in range(HEIGHT):
    for x in range(WIDTH):
           real = REAL_MIN + (x / WIDTH) * (REAL_MAX - REAL_MIN)
           imag = IMAG_MIN + (y / HEIGHT) * (IMAG_MAX - IMAG_MIN)
           c = complex(real, imag)
           image[y, x] = mandelbrot(c)

plt.figure(figsize=(8,8))
plt.imshow(
     image,
     cmap='inferno',
     extent=(REAL_MIN,REAL_MAX,IMAG_MAX,IMAG_MIN)
)
plt.colorbar(label="Escape Iterations")

plt.title("Mandelbrot Set")

plt.xlabel("Real")

plt.ylabel("Imaginary")

plt.show()