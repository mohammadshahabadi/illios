import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# The number of samples we wish to take
num_samples = 1000

# Two arrays in which to store the samples we take
Xs = np.ndarray((num_samples, ))
omegas = np.ndarray((num_samples, ))

for i in range(num_samples):
    # Sample all the parameters from their distributions
    k = 160000.0 + np.random.rand()
    m = 100.0 + (200.0 - 100.0) * np.random.rand()
    y0 = 100 * np.random.rand() * 1e-3
    v = (80.0 + (150.0 - 80.0) * np.random.rand()) * 1e3 / 3600.0
    L = 1.0 + (2.0 - 1.0) * np.random.rand()
    
    # Calculate the angular velocity
    omega = 2.0 * np.pi * v / L
    # Calculate the amplitude
    X = np.abs(k * y0 / (k - m * omega ** 2))

    # Store the samples
    omegas[i] = omega
    Xs[i] = X
fig, ax = plt.subplots()
ax.hist(omegas, density=True)
ax.set_xlabel(r"$\omega$ (1/s)")
ax.set_ylabel(r"$p(\omega)$")
plt.show()