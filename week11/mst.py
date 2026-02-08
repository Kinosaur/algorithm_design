# Kaung Khant Lin
# 6540131
# 542

import sys

# Step 2: Read input
input_data = sys.stdin.read().split()

iterator = iter(input_data)
V = int(next(iterator))
E = int(next(iterator))

edges = []

for _ in range(E):
    u = int(next(iterator))
    v = int(next(iterator))
    w = int(next(iterator))

    # Store as (u, v, weight)
    edges.append((u, v, w))

# Step 3: Sort edges by weight
edges.sort(key=lambda x: x[2])

# Step 4: Disjoint Set (Union-Find) implementation
class DisjointSet:
    def __init__(self, n):
        # Each node is its own parent initially
        self.parent = list(range(n))

    def find(self, i):
        # Find root with path compression
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        # Merge two sets if they're separate
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            self.parent[root_i] = root_j
            return True
        return False  # Cycle detected

# Step 5: Kruskal's Algorithm
ds = DisjointSet(V)

mst_weight = 0
edge_count = 0

for u, v, w in edges:

    if ds.union(u, v):
        # No cycle, include this edge
        mst_weight += w
        edge_count += 1
        
    if edge_count == V - 1:
        break

print(mst_weight)

# Used AI to write the compact comments for the code.