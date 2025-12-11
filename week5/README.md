# Week 5: Dynamic Programming - Edit Distance

## Problem: Minimum Edit Distance

Given two strings A and B, find the minimum number of operations required to transform string A into string B. The allowed operations are:
1. **Insert** a character
2. **Delete** a character
3. **Substitute** a character

This problem is also known as the **Levenshtein Distance**.

### Input/Output
- **Input**: 
  - Line 1: String A
  - Line 2: String B
- **Output**: Minimum edit distance (minimum number of operations)

### Example
```
Input:
FOOD
MONEY

Output:
Minimum Edit Distance: 4
```

**Transformation Steps:**
- FOOD → MOOD (substitute F with M)
- MOOD → MOND (substitute O with N)
- MOND → MONED (insert E)
- MONED → MONEY (substitute D with Y)

---

## Implementations

### version1.py - Naive Recursive Brute Force
- Pure recursive approach without memoization
- Explores all possible edit paths
- For each position (i, j), tries all 3 operations: insert, delete, substitute
- Time complexity: O(3^(m+n)) where m = len(A), n = len(B)
- Exponential time - becomes impractical for longer strings

### version2.py - Recursive with Memoization
- Top-down dynamic programming approach
- Uses memoization dictionary to cache results for each (i, j) state
- Avoids redundant calculations for overlapping subproblems
- Time complexity: O(m × n)
- Space complexity: O(m × n) for memo table

### Recursive Structure

```python
editDistance(i, j):
    # Base cases
    if i == len(A):                     # A is exhausted, insert remaining B
        return len(B) - j
    if j == len(B):                     # B is exhausted, delete remaining A
        return len(A) - i
    
    # Recursive cases
    if A[i] == B[j]:                    # Characters match
        return editDistance(i + 1, j + 1)
    else:                               # Characters don't match
        insert = 1 + editDistance(i, j + 1)
        delete = 1 + editDistance(i + 1, j)
        substitute = 1 + editDistance(i + 1, j + 1)
        return min(insert, delete, substitute)
```

---

## Performance Results

### Version 1: Naive Recursive Brute Force

| Test Case | Running Time (s) |
|-----------|------------------|
| 1.in | 0.000033 |
| 2.in | 0.315824 |
| 3.in | - |
| 4.in | - |
| 5.in | - |
| 6.in | - |
| 7.in | - |
| 8.in | - |

### Version 2: Recursive with Memoization

| Test Case | Running Time (s) |
|-----------|------------------|
| 1.in | 0.000013 |
| 2.in | 0.000026 |
| 3.in | 0.000048 |
| 4.in | 0.007171 |
| 5.in | 0.051775 |
| 6.in | 0.184648 |
| 7.in | 0.514775 |
| 8.in | 0.540281 |

**Note:** `-` indicates timeout/impractical runtime for brute force approach

---

## Test Cases

### Easy Cases (`easy_cases/`)

| Test File | String A | String B | Expected Answer |
|-----------|----------|----------|-----------------|
| 1.in | FOOD | MONEY | 4 |
| 2.in | cVbkWPCnLR | VbkWPQCnLQt | 4 |

### Test Cases (`test_cases/`)

| Test File | Expected Answer | Description |
|-----------|-----------------|-------------|
| 1.in | 4 | Same as easy case 1 |
| 2.in | 4 | Same as easy case 2 |
| 3.in | 22 | Medium difficulty |
| 4.in | 131 | Larger strings |
| 5.in | 490 | Larger strings |
| 6.in | 529 | Larger strings |
| 7.in | 828 | Larger strings |
| 8.in | 942 | Largest test case |

### Input Format
```
String_A
String_B
```

---

## Key Concepts

### Optimal Substructure
The edit distance problem exhibits optimal substructure:

For strings A[0...i] and B[0...j]:
- **If A[i] == B[j]**: $editDistance(i, j) = editDistance(i+1, j+1)$
- **If A[i] ≠ B[j]**:
  - $editDistance(i, j) = 1 + \min \begin{cases} editDistance(i, j+1) & \text{(insert)} \\ editDistance(i+1, j) & \text{(delete)} \\ editDistance(i+1, j+1) & \text{(substitute)} \end{cases}$

### Memoization Benefits
- **Dramatic speedup**: Version 2 is ~12,000x faster on test case 2 (0.315824s → 0.000026s)
- **Handles larger inputs**: Solves test cases 3-8 which timeout with brute force
- **Polynomial complexity**: O(m × n) vs exponential O(3^(m+n))

### Applications
Edit distance is used in:
- **Spell checkers**: Finding similar words
- **DNA sequence alignment**: Comparing genetic sequences
- **Natural language processing**: Text similarity and correction
- **Version control**: Detecting differences in files

---

## Usage

### Run Edit Distance Solutions
```bash
# Version 1: Naive Recursive
python3 version1.py < easy_cases/1.in

# Version 2: With Memoization
python3 version2.py < test_cases/1.in
```

### Expected Output
```
Minimum Edit Distance: 4
Time: 0.000013 seconds
```

---

## Additional Resources

- **Worksheet answers**: Will be available in separate document (contains answers to worksheet5.pdf questions)
- **Performance analysis**: Excel file shows detailed time comparisons

---

## 👤 Author

[Kinosaur](https://github.com/Kinosaur)
