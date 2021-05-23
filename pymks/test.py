import numpy as np
import matplotlib.pyplot as plt

from pymks.datasets import make_microstructure

X_1 = make_microstructure(n_samples=1, grain_size=(25, 25))
X_2 = make_microstructure(n_samples=1, grain_size=(15, 95))

X = np.concatenate((X_1, X_2))

from pymks.tools import draw_microstructures

draw_microstructures(X)

