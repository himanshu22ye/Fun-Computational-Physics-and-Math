# Double Pendulum

A simple Python simulation of a **Double Pendulum** using NumPy and Matplotlib.

This project explores how two connected pendulums move together. Even though the system looks simple, its motion can become highly unpredictable, making it a classic example of **chaos theory**.

---

## Features

- Double pendulum visualization
- Trigonometry-based position calculation
- Animation using Matplotlib
- Clean and beginner-friendly code

---

## Technologies Used

- Python
- NumPy
- Matplotlib

---

## Project Structure

```
double_pendulum/
│
├── main.py
├── README.md
├── output.gif      # Final animation
└── output.png      # Optional preview image
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

---

## Mathematics Used

The position of each bob is calculated using trigonometry.

For the first bob:

```text
x₁ = L₁ × sin(θ₁)
y₁ = -L₁ × cos(θ₁)
```

For the second bob:

```text
x₂ = x₁ + L₂ × sin(θ₂)
y₂ = y₁ - L₂ × cos(θ₂)
```

---

## Output

### Static Double Pendulum

![Output](output.png)

### Animation

![Animation](output.gif)

---

## What I Learned

- Trigonometry in Python
- Coordinate systems
- Matplotlib animation
- Building physics simulations step by step
- Basics of chaotic motion

---

## Future Improvements

- Implement real double pendulum equations
- Add motion trail
- Allow users to change rod lengths and masses
- Export high-quality GIFs

---

This project is part of my **Fun Computational Physics and Math** repository, where I build mathematical and physics simulations using Python.