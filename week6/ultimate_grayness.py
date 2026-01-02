# Kaung Khant Lin
# 6540131
# 542

import sys
import time
sys.setrecursionlimit(10000)

line1 = sys.stdin.readline()
N = int(line1.strip())

v_list = []
d_list = []

for _ in range(N):
    line = sys.stdin.readline()
    v_in, d_in = map(int, line.split())
    v_list.append(v_in)
    d_list.append(d_in)

x = [0] * N          # Global list to store choices (0 or 1)
min_diff = float('inf')
call_count = 0

def solve(i):
    global call_count, min_diff
    call_count += 1
    
    # BASE CASE
    if i == N:
        current_v = 1  # Start multiplication at 1
        current_d = 0  # Start addition at 0
        count = 0      # Count how many items we picked
        
        # Calculate totals based on x
        for j in range(N):
            if x[j] == 1:
                current_v *= v_list[j]
                current_d += d_list[j]
                count += 1
        
        # Pick at least one color
        if count > 0:
            diff = abs(current_v - current_d)
            if diff < min_diff:
                min_diff = diff
        return

    else:
        # RECURSIVE CASE
        
        # Option 1: Skip item i
        x[i] = 0
        solve(i + 1)
        
        # Option 2: Take item i
        x[i] = 1
        solve(i + 1)

start_time = time.time()
solve(0)
end_time = time.time()

print(min_diff)
print(f"Recursive calls: {call_count}")
print(f"Time: {end_time - start_time:.6f} seconds")