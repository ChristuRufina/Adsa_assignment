
def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check if there is a queen in the same column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check upper-left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        
        # Check upper-right diagonal
        for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i][j] == 'Q':
                return False
        
        return True

    def backtrack(board, row):
        if row == n:
            # All queens are placed, add the solution to the result
            solutions.append(["".join(row) for row in board])
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                backtrack(board, row + 1)
                board[row][col] = '.'  # Backtrack

    solutions = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    backtrack(board, 0)
    return solutions

# Example usage:
n = 4
solutions = solve_n_queens(n)

# Print solutions as chessboard representations
for i, solution in enumerate(solutions):
    print(f"Solution {i + 1}:")
    for row in solution:
        print(row)
    print()







"""
Backtracking:
The backtracking method for solving the N-Queens problem is a systematic approach that involves placing queens on a chessboard row by row while ensuring they do not threaten each other.
It employs a recursive strategy to explore possible placements, backtracking when conflicts arise. Safety checks are performed to ensure no queens share the same row, column, or diagonal. Valid solutions are recorded, and the algorithm exhaustively searches for all possible solutions. However, due to its exponential time complexity, the efficiency of this method decreases significantly for larger board sizes.

Time Complexity:
The time complexity of the backtracking algorithm for N-Queens is exponential, specifically O(N!), where N is the size of the chessboard. This is because there are N possibilities for the first row, N-2 possibilities for the second row, N-4 for the third row, and so on. For larger values of N, the number of solutions grows rapidly, making the algorithm less efficient.

Efficiency for Larger N:
The algorithm's efficiency decreases significantly as N increases due to its exponential time complexity. For larger N values, the number of solutions becomes very large, and the algorithm may take a long time to find all solutions. In such cases, more optimized techniques like constraint propagation or simulated annealing may be preferred for solving the N-Queens problem.

"""
