# Mandelbrot Set

This project is my implementation of the **Mandelbrot Set**, one of the most famous fractals in mathematics.

The goal of this project was to understand how a simple mathematical equation can generate an incredibly complex and beautiful pattern.

## What is the Mandelbrot Set?

The Mandelbrot Set is created using the equation:

\[
z_{n+1} = z_n^2 + c
\]

For every point `c` on the complex plane:

1. Start with `z = 0`.
2. Repeatedly calculate `z = z² + c`.
3. If the value of `|z|` becomes greater than 2, the point is considered to have escaped.
4. If it never escapes after a fixed number of iterations, the point is treated as part of the Mandelbrot Set.

The number of iterations before escaping is used to color each pixel, producing the final fractal image.

---

## Features

- Mandelbrot Set generation
- Escape-time algorithm
- Complex number calculations
- Customizable image resolution
- Color visualization using Matplotlib

---

## Technologies Used

- Python
- NumPy
- Matplotlib

---

## How to Run

Clone the repository and run:

```bash
python main.py
```

---

## Output

The program generates an image similar to this:

![Mandelbrot Set](output.png)

---

## What I Learned

While building this project, I learned about:

- Complex numbers in Python
- Fractals
- Mapping pixels to the complex plane
- Nested loops
- Mathematical visualization with Matplotlib
- How simple equations can create complex patterns

---

## Future Improvements

- Interactive zoom
- Smooth coloring
- Higher resolution rendering
- Animation of deep zooms
- Performance optimization using NumPy

---

This project is part of my **Physics-Math-Lab** repository, where I explore mathematics and physics concepts through Python simulations and visualizations.