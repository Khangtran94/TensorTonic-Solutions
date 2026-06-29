import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    total = 0
    for i in range(len(A)):
        total += A[i][i]
    return total
