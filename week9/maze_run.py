# Kaung Khant Lin
# 6540131
# 542

import sys

# --- STEP 3: The State Class ---
class State:
    def __init__(self, r, c, step):
        self.r = r
        self.c = c
        self.step = step
        
    def __repr__(self):
        return f"(({self.r}, {self.c}) step {self.step})"

# --- STEP 2: The Valid Function ---
def is_valid(r, c, M, N, maze):
    # 1. Check Bounds
    if r < 0 or r >= M or c < 0 or c >= N:
        return False
    # 2. Check Wall (1 is wall)
    if maze[r][c] == 1:
        return False
    return True

# --- STEP 10: Helper to Print the Matrix ---
def print_step_matrix(M, N, distance_matrix):
    print("\n--- Expansion Map (Step Counts) ---")
    for r in range(M):
        row_str = ""
        for c in range(N):
            val = distance_matrix[r][c]
            if val == -1: # Unvisited / Wall
                row_str += " . " 
            else:
                row_str += f"{val:2} " # Print number with spacing
        print(row_str)
    print("-" * 20)

def solve():
    # --- STEP 1: Read Input ---
    # Read M and N
    line1 = sys.stdin.readline().split()
    M, N = int(line1[0]), int(line1[1])

    # Read Start
    line2 = sys.stdin.readline().split()
    start_r, start_c = int(line2[0]), int(line2[1])

    # Read Exit
    line3 = sys.stdin.readline().split()
    end_r, end_c = int(line3[0]), int(line3[1])

    # Read Maze
    maze = []
    for i in range(M):
        maze.append([int(x) for x in sys.stdin.readline().split()])

    # --- STEP 4 & 9: BFS Initialization ---
    
    # 1. The Queue (Start with entrance)
    start_state = State(start_r, start_c, 0) # Step 0 at start
    Q = [start_state] 
    
    # 2. The Visited Tracker (Optimization from Step 9)
    #    Keeps track of where we have been. Initialize with False.
    visited = [[False for _ in range(N)] for _ in range(M)]
    visited[start_r][start_c] = True

    # 3. Distance Matrix (For Step 10 Printing)
    #    Initialize with -1. We will fill this with step counts.
    dist_matrix = [[-1 for _ in range(N)] for _ in range(M)]
    dist_matrix[start_r][start_c] = 0

    # 4. Directions (Up, Down, Left, Right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 5. Counter (Step 5)
    state_count = 1  # We created 1 state so far (start)

    print(f"Start Search: ({start_r}, {start_c}) -> Goal: ({end_r}, {end_c})")

    final_step = -1
    
    while len(Q) > 0:
        # Pop the oldest state (First In, First Out)
        current = Q.pop(0)
        
        # Check if we found the exit
        if current.r == end_r and current.c == end_c:
            final_step = current.step
            break # Found it! Stop searching.

        # Expand to neighbors
        for dr, dc in directions:
            new_r = current.r + dr
            new_c = current.c + dc
            
            # Check if valid AND NOT VISITED
            if is_valid(new_r, new_c, M, N, maze) and not visited[new_r][new_c]:
                
                # Create new state
                new_step = current.step + 1
                new_state = State(new_r, new_c, new_step)
                
                # Add to Queue
                Q.append(new_state)
                
                # Mark as visited (So we don't process it again)
                visited[new_r][new_c] = True
                dist_matrix[new_r][new_c] = new_step
                state_count += 1

    # Step 10: Show the map
    print_step_matrix(M, N, dist_matrix)
    
    print(f"\nStates Constructed: {state_count}")
    
    if final_step != -1:
        print(f"Shortest Route: {final_step}")
    else:
        print("No path found.")

if __name__ == "__main__":
    solve()
    
    
# Used AI for formatting write proper comments