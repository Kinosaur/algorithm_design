import sys

def solve():
    line1 = sys.stdin.readline()
    n = int(line1.strip())
    
    line2 = sys.stdin.readline()
    prices = list(map(int, line2.split()))

    dp = [0.0] * (n + 1)
    
    for i in range(1, n + 1):
        current_p = prices[i-1]
        
        # OPTION 1: Buy Single
        dp[i] = dp[i-1] + current_p
        
        # OPTION 2: Pair Deal (Only if we have at least 2 shoes)
        if i >= 2:
            prev_p = prices[i-2]
            # Calculate cost of this group
            group_sum = current_p + prev_p
            discount = min(current_p, prev_p) / 2.0
            cost_this_group = group_sum - discount
            
            # Compare with current best
            dp[i] = min(dp[i], dp[i-2] + cost_this_group)
            
        # OPTION 3: Trio Deal (Only if we have at least 3 shoes)
        if i >= 3:
            prev_p = prices[i-2]
            prev_prev_p = prices[i-3]
            # Calculate cost of this group
            group_sum = current_p + prev_p + prev_prev_p
            discount = min(current_p, prev_p, prev_prev_p)
            cost_this_group = group_sum - discount
            
            # Compare with current best
            dp[i] = min(dp[i], dp[i-3] + cost_this_group)
            
    print(f"{dp[n]:.1f}")

if __name__ == "__main__":
    solve()