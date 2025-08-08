# test simple maths
import numpy as np
import matplotlib.pyplot as plt

# Generate x values
x = np.linspace(0, 5)

# Calculate y values
y = 4 ** (x - 3)

# Plot the curve
plt.plot(x, y)
plt.title('Curve of \(4^{x-3}\)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
