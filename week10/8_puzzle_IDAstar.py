# Kaung Khant Lin
# 6540131
# 542

import sys
import copy

sys.setrecursionlimit(20001)

n = 9
d = 3
p = []
for i in range(d):
    p += list(map(int, input().split()))


def valid(i, j):
    global d

    if i >= 0 and i < d and j >= 0 and j < d:
        return True
    else:
        return False


class State:
    def __init__(self, p):
        self.p = copy.deepcopy(p)
        self.g = 0
        self.h = 1000000000


def manhattan(p):
    # The heuristic lowerbound on the required number of moves
    # Manhattan distance == 0 indicates the goal state

    h = 0
    for i in range(len(p)):
        if p[i] != 0:
            tr = i // d
            tc = i % d
            r = p[i] // d
            c = p[i] % d
            h += abs(tr - r) + abs(tc - c)
    return h


adj = [(0, -1), (0, 1), (1, 0), (-1, 0)]


def successor(s):
    global d

    succ = []
    for i in range(len(s.p)):
        if s.p[i] == 0:
            hole = i
            break
    r = hole // d
    c = hole % d
    for a in adj:
        i = r + a[0]
        j = c + a[1]
        if valid(i, j):
            target = i * d + j
            m = s.p[:]
            m[target], m[hole] = m[hole], m[target]
            u = State(m)
            u.g = s.g + 1
            u.h = manhattan(m)
            succ.append(u)
    return succ


def DFS(s, atMost):
    global count, found

    if s.g + s.h > atMost:
        return s.g + s.h
    elif s.h == 0:
        found = True
        return s.g
    else:
        count += 1
        atLeast = 10000000000
        for u in successor(s):
            atLeast = min(atLeast, DFS(u, atMost))
            if found:
                break
        return atLeast


def IDAstar(s):
    global found

    # Set the initial threshold to the heuristic value of the start state
    threshold = s.h

    # Loop until the goal is found
    while True:
        # DFS returns either the solution cost (if found)
        # or the next threshold value (if not found)
        temp = DFS(s, threshold)

        # If goal is found, return the cost
        if found:
            return temp

        # If not found, update the threshold for the next iteration
        # The DFS function calculates the minimum f-value that exceeded the previous threshold
        threshold = temp

        # Safety check: if threshold becomes infinite, no solution exists
        if threshold > 1000000000:
            return -1


count = 0
s = State(p)
s.h = manhattan(s.p)
if s.h == 0:
    found = True
else:
    found = False
print(IDAstar(s))
print("state count = ", count)
