# Week 2: Recursion and Combinatorics


## Overview

This week focuses on **recursive algorithms** and **combinatorics**, specifically exploring:
- Binary combinations (2^n possibilities)
- Combinations with k selections (C(n,k))
- Multi-option combinations (3^n possibilities)
- Practical application: Balance Split Problem

---

## Files

### Core Implementation Files

| File | Description |
|------|-------------|
| `factorial.py` | Helper module providing factorial function for combination calculations |
| `task1.py` | Basic binary combination generator (2^n combinations) |
| `task2.py` | Extended combination examples with counting and k-selections |
| `ans.py` | Clean implementation of binary combination generator |
| `balanceSplit.py` | Balance Split problem - Version 1 (using decision array) |
| `balanceSplit2.py` | Balance Split problem - Version 2 (optimized with running sum) |

### Test Cases

Located in `balanceSplit/` directory:

| Test File | Input | Expected Answer |
|-----------|-------|-----------------|
| `1.in` | 5 items: 2627 67536 70013 14133 64027 | 44790 |
| `2.in` | 10 items: 40269 57181 56421 ... | 30 |
| `3.in` | 10 items: 30564 72006 71139 ... | 603 |
| `4.in` | 10 items: 96376 2440 88670 ... | 70 |
| `5.in` | 10 items: 82653 33778 55465 ... | 459 |

---

## Concepts

### 1. Binary Combinations (2^n)

Generate all possible combinations where each item can be either selected (1) or not selected (0).

```
For n=3: 000, 001, 010, 011, 100, 101, 110, 111 (8 combinations)
```

**Implementation:** `task1.py`, `ans.py`

### 2. Combinations with k Selections (C(n,k))

Generate combinations where exactly k items are selected from n items.

**Formula:** $C(n,k) = \frac{n!}{k!(n-k)!}$

**Implementation:** `task2.py` - `comb_k_1()` function

### 3. Multi-option Combinations (3^n)

Each item has 3 choices (0, 1, or 2) instead of binary choices.

**Implementation:** `task2.py` - `comb3()` function

---

## Balance Split Problem

### Problem Statement

Given a list of n positive integers, split them into two groups (A and B) such that the absolute difference between the sum of group A and group B is minimized.

### Approach

**Version 1 (`balanceSplit.py`):**
- Uses a decision array `x[]` to track which group each item belongs to
- At base case, iterates through array to calculate both sums
- Time complexity: O(2^n × n)

**Version 2 (`balanceSplit2.py`):**
- Optimized by passing running sum as parameter
- Calculates `sum_b = total_sum - sum_a` directly
- Time complexity: O(2^n)

### Algorithm Pattern

```
solve(i):
    if i == n:                    # Base case: all items assigned
        calculate difference
        update minimum if better
        return
    
    # Recursive case
    Put item[i] in Group A → solve(i+1)
    Put item[i] in Group B → solve(i+1)
```

---

## Usage

### Running Combination Generators

```bash
python task1.py
# Enter the number of items: 3

python task2.py
# Enter the number of items: 3
# Enter k (number of 1's): 2
```

### Running Balance Split

```bash
# Version 1
python balanceSplit.py < balanceSplit/1.in

# Version 2 (optimized)
python balanceSplit2.py < balanceSplit/1.in
```

**Expected Output:**
```
Minimal Difference: 44790
Time: X.XXXXXX seconds
```

---

## Time Complexity Analysis

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Binary Combinations | O(2^n) | O(n) |
| k-Combinations | O(2^n) | O(n) |
| 3-Option Combinations | O(3^n) | O(n) |
| Balance Split v1 | O(2^n × n) | O(n) |
| Balance Split v2 | O(2^n) | O(n) |

---

## Notes

- The Balance Split solutions use pure recursive enumeration without pruning optimizations
- AI was used for conceptual explanations; all code was written independently based on understanding
- Recursion limit is set to 10000 for deeper recursive calls

---

## Learning Outcomes

1. Understanding recursive enumeration patterns
2. Generating all binary combinations systematically
3. Applying combinations to optimization problems
4. Comparing algorithmic approaches (decision array vs. running sum)

## 👤 Author

[Kinosaur](https://github.com/Kinosaur)
