# Fourier Series - Square Wave

This project demonstrates how a **square wave** can be approximated by adding multiple sine waves together using the **Fourier Series**.

The goal of this project was to understand how a complex waveform can be created from simple mathematical functions and to visualize the result using Python.

---

## Mathematical Formula

The Fourier Series for a square wave is:

\[
f(x)=\frac{4}{\pi}\left(\sin(x)+\frac{1}{3}\sin(3x)+\frac{1}{5}\sin(5x)+\cdots\right)
\]

Only **odd harmonics** (1, 3, 5, 7, ...) are used.

As more harmonics are added, the waveform becomes closer to an ideal square wave.

---

## Features

- Fourier Series implementation in Python
- Square wave approximation
- Uses odd harmonics
- Mathematical visualization using Matplotlib
- High-resolution output image

---

## Technologies Used

- Python
- NumPy
- Matplotlib

---

## Project Structure

```
fourier_series/
│
├── main.py
├── README.md
└── output.png
```

---

## How to Run

Install the required libraries:

```bash
pip install numpy matplotlib
```

Run the program:

```bash
python main.py
```

The graph will be displayed and saved as **output.png**.

---

## Output

![Fourier Series Output](output.png)

---

## What I Learned

While building this project, I learned about:

- Fourier Series
- Harmonics
- Sine waves
- NumPy arrays
- Mathematical visualization
- Plotting graphs using Matplotlib

---

## Future Improvements

- Animate the wave as harmonics are added
- Interactive slider to change the number of harmonics
- Support for triangle and sawtooth waves
- Fourier epicycle visualization

---

This project is part of my **Fun-Computational-Physics-and-Math** repository, where I explore mathematics and physics concepts through Python simulations and visualizations.