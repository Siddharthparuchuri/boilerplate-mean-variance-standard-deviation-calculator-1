import numpy as np

def calculate(data):
    """Calculates statistics for a 3x3 matrix.

    Args:
        data: A list of 9 numbers representing the matrix elements.

    Returns:
        A dictionary containing mean, variance, standard deviation, max, 
        min, and sum for rows, columns, and the flattened matrix.

    Raises:
        ValueError: If the input list has less than 9 elements.
    """

    if len(data) != 9:
        raise ValueError("List must contain nine numbers.")

    # Convert the list to a NumPy array and reshape to a 3x3 matrix
    arr = np.array(data).reshape(3, 3)

    # Calculate statistics along both axes and for the flattened array
    results = {
        'mean': [arr.mean(axis=1).tolist(), arr.mean(axis=0).tolist(), arr.mean().tolist()],
        'variance': [arr.var(axis=1).tolist(), arr.var(axis=0).tolist(), arr.var().tolist()],
        'standard deviation': [arr.std(axis=1).tolist(), arr.std(axis=0).tolist(), arr.std().tolist()],
        'max': [arr.max(axis=1).tolist(), arr.max(axis=0).tolist(), arr.max().tolist()],
        'min': [arr.min(axis=1).tolist(), arr.min(axis=0).tolist(), arr.min().tolist()],
        'sum': [arr.sum(axis=1).tolist(), arr.sum(axis=0).tolist(), arr.sum().tolist()]
    }

    return results

if __name__ == "__main__":
    data = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    stats = calculate(data)
    print(stats)
