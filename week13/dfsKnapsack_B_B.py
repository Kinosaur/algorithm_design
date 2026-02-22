# Kaung Khant Lin
# 6540131
# 542

class obj:
    def __init__(self, w, v):
        self.w = w
        self.v = v
        self.r = v / w

x = input().split()
N = int(x[0])
M = int(x[1])
w = input().split()
v = input().split()

item = []
for i in range(N):
    item.append(obj(int(w[i]), int(v[i])))

# Sort items by value-to-weight ratio in descending order
def getKey(x):
    return x.r

item.sort(key=getKey, reverse=True)

maxV = 0

# Step 3
recursion_count = 0 

# Step 9: The Bounding Function (Pasted from KnapsackBound.py)
def Bound(i, C):
    global item, N
    sw = 0
    sv = 0
    j = i
    f = 1.0
    while j < N and f == 1.0:
        wj = min(C - sw, item[j].w)
        f = float(wj) / item[j].w
        sw += f * item[j].w
        sv += f * item[j].v
        j += 1
    return sv

# Step 11: DFS with Best-First Branch & Bound
def dfs(i, sumW, sumV):
    global maxV, item, N, M, recursion_count

    # Count every recursive call
    recursion_count += 1

    # Pruning
    optimistic_estimate = sumV + Bound(i, M - sumW)
    if optimistic_estimate <= maxV:
        return

    # Base Case
    if i == N:
        if sumW <= M:
            maxV = max(maxV, sumV)
        return

    # Estimate bounds for Take and Skip
    bound_take = 0
    if sumW + item[i].w <= M:
        bound_take = sumV + item[i].v + Bound(i + 1, M - (sumW + item[i].w))

    bound_skip = sumV + Bound(i + 1, M - sumW)

    # Explore higher bound first
    if bound_take > bound_skip:
        if bound_take > maxV and sumW + item[i].w <= M:
            dfs(i + 1, sumW + item[i].w, sumV + item[i].v)
        if bound_skip > maxV:
            dfs(i + 1, sumW, sumV)
    else:
        if bound_skip > maxV:
            dfs(i + 1, sumW, sumV)
        if bound_take > maxV and sumW + item[i].w <= M:
            dfs(i + 1, sumW + item[i].w, sumV + item[i].v)

dfs(0, 0, 0)
print(maxV)
print(recursion_count)