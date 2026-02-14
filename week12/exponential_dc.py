# Kaung Khant Lin
# 6540131
# 542

def dc_exponential(a, x):
    # Base cases
    if x == 0:
        return 1
    if x == 1:
        return a
    
    # Divide: Calculate a^(x/2) once
    half_power = dc_exponential(a, x // 2)
    
    # Combine
    if x % 2 == 0:
        return half_power * half_power
    else:
        return a * half_power * half_power

# Running Time: O(log n) where n is the exponent x
# Reason: The problem size (exponent) is halved in every recursive step.

print(dc_exponential(2, 10))