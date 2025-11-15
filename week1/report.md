# Maximum Contiguous Subsequence - Performance Report

**Name:** Kaung Khant Lin  
**Student ID:** 6540131  
**Section:** 542

---

## Test Cases Running Time Comparison

### Approach 1: Straightforward Solution (O(n³))
File: `maxsum_v1.py`

| Test Case | Size (n) | Running Time (seconds) |
|-----------|----------|------------------------|
| 10.in     | 10       | 2.199999999999945e-05  |
| 50.in     | 50       | 0.0005629999999999993  |
| 100.in    | 100      | 0.00375  |
| 1000.in   | 1000     | 3.536434  |
| 10000.in  | 10000    | still don't finish yet after writing this report |
| 25600.in  | 25600    |          -              |
| 100000.in | 100000   |            -            |

---

### Approach 2: Accumulation Technique (O(n²))
File: `maxsum_v2.py`

| Test Case | Size (n) | Running Time (seconds) |
|-----------|----------|------------------------|
| 10.in     | 10       | 1.2999999999999123e-05 |
| 50.in     | 50       | 0.00013400000000000044 |
| 100.in    | 100      | 0.0005010000000000014 |
| 1000.in   | 1000     | 0.050244 |
| 10000.in  | 10000    | 4.214038 |
| 25600.in  | 25600    | 27.979069000000003 |
| 100000.in | 100000   |          -         |

---

### Approach 3: Kadane's Algorithm (O(n))
File: `maxsum_v3.py`

| Test Case | Size (n) | Running Time (seconds) |
|-----------|----------|------------------------|
| 10.in     | 10       | 7.000000000000062e-06  |
| 50.in     | 50       | 1.3000000000000858e-05 |
| 100.in    | 100      | 1.700000000000139e-05  |
| 1000.in   | 1000     | 0.00011399999999999952 |
| 10000.in  | 10000    | 0.00098                |
| 25600.in  | 25600    | 0.002274               |
| 100000.in | 100000   | 0.008877               |

---

## Analysis

### Time Complexity Comparison

| Approach | Time Complexity | Description |
|----------|----------------|-------------|
| Approach 1 | O(n³) | Straightforward solution using nested loops with sum calculation |
| Approach 2 | O(n²) | Uses prefix sum array for constant-time sum calculation |
| Approach 3 | O(n) | Kadane's Algorithm - optimal linear time solution |