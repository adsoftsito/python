# create virtual environment 
1. python -m venv pymks

# activate
2. source pymks/bin/activate

# install package

3. pip install pymks

# create test.py
4. vi test.py

import numpy as np
import matplotlib.pyplot as plt

from pymks.datasets import make_microstructure

X_1 = make_microstructure(n_samples=1, grain_size=(25, 25))
X_2 = make_microstructure(n_samples=1, grain_size=(15, 95))

X = np.concatenate((X_1, X_2))

from pymks.tools import draw_microstructures

draw_microstructures(X)

# run
5. python test.py


