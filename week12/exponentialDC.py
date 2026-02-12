# a ** x without **
def sf_exponential(a, x):
    result = 1
    for _ in range(x):
        result = result * a
    return result

print(sf_exponential(2, 10))

def dc_exponential(a, x):
    # Base cases
    if x == 0:
        return 1
    if x == 1:
        return a
    
    # Divide
    half_power = dc_exponential(a, x // 2)
    
    if x % 2 == 0:
        return half_power * half_power
    else:
        return a * half_power * half_power

print(dc_exponential(2, 10))