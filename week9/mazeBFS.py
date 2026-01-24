import sys

# Step 3: Define the State class
class State:
    def __init__(self, r, c, step):
        self.r = r
        self.c = c
        self.step = step
        
    # This magic method __repr__ makes the object print nicely
    # Instead of <__main__.State object at 0x...>, it will print: ((0, 0) step 0)
    def __repr__(self):
        return f"(({self.r}, {self.c}) step {self.step})"

# Step 2: Implement the is_valid function
def is_valid(r, c, M, N, maze):
    # Check if (r, c) is inside the grid AND not a wall
    if 0 <= r < M and 0 <= c < N and maze[r][c] == 0:
        return True
    return False

def solve():
    # Step 1: Read input
    line1 = sys.stdin.readline().split()
    M, N = int(line1[0]), int(line1[1])

    line2 = sys.stdin.readline().split()
    start_r, start_c = int(line2[0]), int(line2[1])

    line3 = sys.stdin.readline().split()
    end_r, end_c = int(line3[0]), int(line3[1])

    maze = []
    for i in range(M):
        maze.append([int(x) for x in sys.stdin.readline().split()])

    # --- TESTING THE VALID FUNCTION ---
    # Let's test a few points from our sample input
    test_points = [
        (0, 0), # Start (Should be True)
        (0, 1), # Wall (Should be False)
        (-1, 0),# Out of bounds (Should be False)
        (3, 4)  # End (Should be True)
    ]
    
    print(f"Map Size: {M}x{N}")
    for r, c in test_points:
        result = is_valid(r, c, M, N, maze)
        print(f"Is ({r}, {c}) valid? -> {result}")
    
    print("\n--- TESTING THE STATE CLASS ---")
    # 1. Create the start state (Row 0, Col 0, Step 0)
    current_state = State(0, 0, 0)
    print(f"Start: {current_state}") 

    # 2. Simulate moving Down (Row + 1)
    # We take the old step (0) and add 1
    next_state = State(current_state.r + 1, current_state.c, current_state.step + 1)
    print(f"Moved Down: {next_state}")

if __name__ == "__main__":
    solve()