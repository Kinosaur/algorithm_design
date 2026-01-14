#Phanthira Kositjaroenkul 6630003

m = int(input())
n = int(input())
memo={}
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

def min_path(grid, i, j):
    if i == m-1 and j== n-1:
        memo=grid[m-1][n-1]
        return grid[m-1][n-1]
    if i >= m or j >= n:
        min_path = float('inf')
        return min_path

    return grid[i][j] + min(min_path(grid, i+1, j), min_path(grid,i,j+1))

print(min_path(grid,0,0))
