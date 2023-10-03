# Input list of matrices
matrices = [(2, 3), (3, 4), (4, 2)]

# Number of matrices
n = len(matrices) - 1

# Initialize a table for storing minimum multiplications
m = [[0] * (n+1) for _ in range(n+1)]

# Initialize a table for tracking optimal splits
s = [[0] * (n+1) for _ in range(n+1)]

# Initialization: Setting the base case values
for i in range(1, n+1):
    m[i][i] = 0

# Filling in the tables using dynamic programming
for chain_len in range(2, n+1):  # Chain length from 2 to n
    for i in range(1, n - chain_len + 2):
        j = i + chain_len - 1
        m[i][j] = float('inf')  # Set initial value to infinity
        for k in range(i, j):
            cost = m[i][k] + m[k+1][j] + matrices[i-1][0] * matrices[k][1] * matrices[j][1]
            if cost < m[i][j]:
                m[i][j] = cost
                s[i][j] = k

# Reconstruct the optimal parenthesization
def print_optimal_parenthesis(s, i, j):
    if i == j:
        print(f'M{str(i)}', end='')
    else:
        print("(", end='')
        print_optimal_parenthesis(s, i, s[i][j])
        print_optimal_parenthesis(s, s[i][j]+1, j)
        print(")", end='')

print("Optimal Parenthesization:")
print_optimal_parenthesis(s, 1, n)
print("\n")

# Minimum number of scalar multiplications for the optimal parenthesization
min_scalar_multiplications = m[1][n]
print(f"Minimum Scalar Multiplications: {min_scalar_multiplications}")




"""
Explanation:
dims is a list of dimensions of the matrices where dims[i] represents the number of rows of matrix i and dims[i+1] represents the number of columns of matrix i.
m[i][j] stores the minimum number of scalar multiplications needed to compute the product of matrices from i to j.
s[i][j] keeps track of the optimal split position.

Time Complexity:
The time complexity of this dynamic programming algorithm is O(n^3) because we fill in two tables (m and s) of size O(n^2) and compute each entry in these tables in constant time.

Space Complexity:
The space complexity is O(n^2) for storing the m and s tables.

Efficiency:
This algorithm efficiently finds the optimal parenthesization and the minimum scalar multiplications for a given sequence of matrices, making it suitable for large instances of the problem.

"""
