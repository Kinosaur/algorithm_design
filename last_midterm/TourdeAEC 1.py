# Dynamic Programming - Bottom Up
#Phanthira Kositjaroenkul 6630003

NList=list(input())
MList=list(input())

N=len(NList)
M=len(MList)

# Dynamic Programming - Bottom Up

dp = [[0] * (N + 1) for _ in range(M + 1)]

for i in range(1, M + 1):
    for j in range(1, N + 1):
        if NList[i-1]==MList[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            

# The bottom-right cell contains the length of LCS
print(dp[N][M])