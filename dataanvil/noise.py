import numpy as np

def add_gaussian_noise(X, sigma=0.1, random_state=None):
    rng = np.random.default_rng(random_state)
    noise = rng.normal(0, sigma, X.shape)
    return X + noise
