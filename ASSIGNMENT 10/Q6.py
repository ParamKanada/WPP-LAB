"""The bisection method is a technique for finding solutions (roots) to equations with a single
unknown variable. Given a polynomial function f, try to find an initial interval off by
random probe. Store all the updates in an Numpy array. Plot the root finding process using
the matplotlib/pyplot library."""

import numpy as np
import matplotlib.pyplot as plt

# Define the polynomial function
def f(x):
    return x**3 - 6*x**2 + 11*x - 6  # Example polynomial: (x - 1)(x - 2)(x - 3)

# Bisection method implementation
def bisection_method(func, a, b, tol=1e-6):
    updates = []
    if func(a) * func(b) >= 0:
        raise ValueError("The function must have opposite signs at endpoints a and b.")

    while abs(b - a) > tol:
        c = (a + b) / 2  # Midpoint
        updates.append((a, b, c, func(c)))  # Store interval and function value
        if func(c) == 0:  # Found the root
            break
        elif func(a) * func(c) < 0:
            b = c
        else:
            a = c

    updates.append((a, b, c, func(c)))  # Final update
    return np.array(updates)

# Plotting the process
def plot_root_finding(updates, func):
    x_vals = np.linspace(min(updates[:, 0]), max(updates[:, 1]), 500)
    y_vals = func(x_vals)

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label="f(x)", color="blue")
    plt.axhline(0, color="black", linestyle="--", linewidth=0.8)
    plt.title("Bisection Method Root-Finding Process")
    plt.xlabel("x")
    plt.ylabel("f(x)")

    for i, (a, b, c, _) in enumerate(updates):
        plt.plot([a, b], [0, 0], marker="o", label=f"Iteration {i+1}" if i == 0 else "")

    plt.legend()
    plt.grid()
    plt.show()

# Main program
try:
    a, b = np.random.uniform(-10, 10, 2)  # Random interval
    a, b = min(a, b), max(a, b)  # Ensure a < b
    updates = bisection_method(f, a, b)
    print("Updates (a, b, c, f(c)):")
    print(updates)

    # Plot the root-finding process
    plot_root_finding(updates, f)
except ValueError as e:
    print(e)