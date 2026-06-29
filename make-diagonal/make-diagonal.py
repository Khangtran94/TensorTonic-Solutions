import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    # Write code here
    n = len(v)
    return np.array([[v[i] if i == j else 0 for j in range(n)] for i in range(n)])
