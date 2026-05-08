import numpy as np

def zscore_standardize(X, axis=0, eps=1e-12):
    """
    Standardize X: (X - mean)/std. If 2D and axis=0, per column.
    Return np.ndarray (float).
    """
    # Write code here
    if axis == 0:
        cols = list(zip(*X))
        z_cols = []
        for col in cols:
            avg_col = np.mean(col)
            std_col = np.std(col)
            z_col_values = [(x - avg_col) / (std_col + eps) for x in col]
            z_cols.append(z_col_values)
        return np.array(z_cols).T
    else:
        z_rows = []
        for row in X:
            avg_row = np.mean(row)
            std_row = np.std(row)
            z_row_values = [(x - avg_row) / (std_row + eps) for x in row]
            z_rows.append(z_row_values)
        return z_rows
    pass