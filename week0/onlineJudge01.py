# Kaung Khant Lin
# 6540131
# 542

# Problem: Minimum Cost to Buy Exact K kg of Apples with N Packets

def find_min_cost(max_packets, target_kg, prices):
    # dp[w] = min cost to buy exactly w kg, -1 means impossible
    dp = [-1] * (target_kg + 1)
    dp[0] = 0
    
    # try using 1 packet, then 2 packets, up to max_packets
    for num_packets in range(1, max_packets + 1):
        new_dp = dp[:]
        
        for kg in range(1, target_kg + 1):
            # try buying each available packet size
            for packet_kg in range(1, kg + 1):
                packet_cost = prices[packet_kg - 1]
                
                if packet_cost != -1:
                    remaining = kg - packet_kg
                    
                    if dp[remaining] != -1:
                        total_cost = dp[remaining] + packet_cost
                        
                        if new_dp[kg] == -1:
                            new_dp[kg] = total_cost
                        else:
                            new_dp[kg] = min(new_dp[kg], total_cost)
        
        dp = new_dp
    
    return dp[target_kg]


test_cases = int(input())

for _ in range(test_cases):
    n, k = map(int, input().split())
    prices = list(map(int, input().split()))
    
    result = find_min_cost(n, k, prices)
    print(result)