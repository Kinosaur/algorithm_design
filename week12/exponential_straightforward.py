# Kaung Khant Lin
# 6540131
# 542

def sf_exponential(a, x):
    result = 1
    # Loop runs x times
    for _ in range(x):
        result = result * a
    return result

# Running Time: O(n) where n is the exponent x
# Reason: The loop iterates exactly x times.

print(sf_exponential(2, 10))