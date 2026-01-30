# Kaung Khant Lin
# 6540131
# 542

from sys import stdin
from SimplePriorityQueue import SimplePriorityQueue

INF = 10000000000
V = int(input())
adj = [[] for i in range(V)]

for line in stdin:
    x = line.split()
    u = int(x[0])
    v = int(x[1])
    w = int(x[2])
    adj[u].append((v,w))
    adj[v].append((u,w))


class State:
    def __init__(self, city, d):
        self.city = city
        self.d = d

def successor(s):
    global shortest

    succ = []
    for a in adj[s.city]:
        v = a[0]
        w = a[1]
        if s.d + w < shortest[v]:
            shortest[v] = s.d + w
            succ.append(State(v, s.d+w))
    return succ

shortest = [INF]*V

def cityCompare(x, y):
    return x.d < y.d

# Write UCS code below this line
pq = SimplePriorityQueue(cityCompare)

# Initial State
start_node = State(0, 0)
shortest[0] = 0
pq.enqueue(start_node)

# Loop until queue is empty
while not pq.empty():
    s = pq.dequeue()

    # from city 0 to n-1
    if s.city == V - 1:
        break

    # Expand the node -> Put successor function
    neighbors = successor(s)

    # enqueue neighbors
    for neighbor in neighbors:
        pq.enqueue(neighbor)

print(s.d)

