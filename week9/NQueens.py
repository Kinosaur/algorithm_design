# Kaung Khant Lin
# 6540131
# 542

from print_queens import print_queens
from collections import deque
import copy

class State():
    def __init__(self, n):
        self.queen_list = [-1]*n
        self.column = 0

def is_conflict(queen_list, current_col, row):
    for col in range(current_col):
        prev_row = queen_list[col]
        
        # 1. Check if in the same row
        if prev_row == row:
            return True
            
        # 2. Check if in the same diagonal
        if abs(prev_row - row) == abs(col - current_col):
            return True
            
    return False

def solve_n_queens(n):
    # Create the initial empty state
    initial_state = State(n)
    
    queue = deque([initial_state])
    solutions = []
    
    while queue:
        current_state = queue.popleft()
        
        # Check the goal condition
        if current_state.column == n:
            solutions.append(list(current_state.queen_list))
            continue

        
        col = current_state.column
        # Copy the current state
        # Place the queen in the copy
        # Move to the next column
        # Put the new state into the queue
        for row in range(n):
            if not is_conflict(current_state.queen_list, col, row):
                next_state = copy.deepcopy(current_state)
                next_state.queen_list[col] = row
                next_state.column += 1
                queue.append(next_state)
        
    return solutions

if __name__ == "__main__":
    input_str = input("Enter number of queens (N): ")
    N = int(input_str)
        
    print(f"Solving for {N}-Queens...")
    solutions = solve_n_queens(N)
    
    if solutions:
        print(f"Found {len(solutions)} solution(s) for {N}-Queens.")
        for idx, sol in enumerate(solutions, start=1):
            print(f"Solution {idx}:")
            print_queens(sol)
            print("Raw list:", sol)
    else:
        print(f"No solution found for {N}-Queens.")
