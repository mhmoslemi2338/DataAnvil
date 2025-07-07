import numpy as np
from Anvil.noise import add_gaussian_noise

def test_add_gaussian_noise_shape():
    X = np.ones((10, 5))
    X_noisy = add_gaussian_noise(X, sigma=0.1)
    assert X_noisy.shape == X.shape
