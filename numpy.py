import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve
from scipy.optimize import curve_fit

# -----------------------------------------------
# Step 1: NumPy Operations
# -----------------------------------------------
def numpy_operations():
    arr = np.array([1, 2, 3, 4, 5])
    print("NumPy Array:", arr)
    print("Sum:", np.sum(arr))
    print("Mean:", np.mean(arr))
    print("Standard Deviation:", np.std(arr))
    print("Max:", np.max(arr))
    print("Min:", np.min(arr))

    arr2 = np.array([1, 2, 3, 4, 5, 6])
    reshaped_arr = arr2.reshape((2, 3))
    print("Reshaped Array:\n", reshaped_arr)

# -----------------------------------------------
# Step 2: Solving Linear Equations with SciPy
# -----------------------------------------------
def solve_linear_equations():
    A = np.array([[3, 2], [4, 3]])
    B = np.array([5, 6])

    solution = solve(A, B)
    print("\nSolution to the system of equations [3x + 2y = 5, 4x + 3y = 6]:")
    print("Solution [x, y]:", solution)

# -----------------------------------------------
# Step 3: Plotting Data and Fitting a Curve with Matplotlib
# -----------------------------------------------
def plot_and_fit_curve():
    # Generate some noisy data
    np.random.seed(0)
    x = np.linspace(0, 10, 100)
    y = 2 * x + 1 + np.random.normal(0, 1, size=x.size)  # Linear data with noise

    # Define the linear model
    def linear_model(x, a, b):
        return a * x + b

    # Fit the model to the data
    params, _ = curve_fit(linear_model, x, y)

    # Plot the noisy data and the fitted line
    plt.scatter(x, y, label="Noisy data")
    plt.plot(x, linear_model(x, *params), color='red', label=f"Fitted line: y = {params[0]:.2f}x + {params[1]:.2f}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Linear Fit to Noisy Data")
    plt.legend()
    plt.show()

# -----------------------------------------------
# Main Function
# -----------------------------------------------
def main():
    print("Step 1: NumPy Operations")
    numpy_operations()

    print("\nStep 2: Solving Linear Equations")
    solve_linear_equations()

    print("\nStep 3: Plotting and Curve Fitting")
    plot_and_fit_curve()

if __name__ == "__main__":
    main()
