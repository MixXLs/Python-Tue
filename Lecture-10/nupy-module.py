import numpy as np

randow_matrix = np.random.randint(1, 11, size = (3, 3))
print("Random 3x3 Matrix:\n", randow_matrix)

matrix_sum = np.sum(randow_matrix)
print(f"\nSum of all elemenntsL {matrix_sum}")

matrix_mean = np.mean(randow_matrix)
print(f"\nMean of the matrix: {matrix_mean:2.2f}")

transposed_matrix = np.transpose(randow_matrix)
print(f"\nTransposed Matrix:\n", transposed_matrix)