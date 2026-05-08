import numpy as np

def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    # Write code here
    if axis == 0:
        cols = list(zip(*X))
        norm_cols = []
        for col in cols:
            max_col = max(col)
            min_col = min(col)
            norm_col_values = [(x - min_col) / (max_col - min_col + eps) for x in col]
            norm_cols.append(norm_col_values)
        return np.array(norm_cols).T
    else:
        norm_rows = []
        for row in X:
            max_row = max(row)
            min_row = min(row)
            norm_row_value = [(x - min_row) / (max_row - min_row + eps) for x in row]
            norm_rows.append(norm_row_value)
        return norm_rows
    pass