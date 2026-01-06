# Binary Image Tensor Gate Decomposition - Competitive Programming Problem

## Overview

An original Div1/Div2 competitive programming problem combining:

- 🖼️ **Image processing** (binary pixel matrices)
- 🔢 **Tensor decomposition** (rank-1 outer products)
- ⚡ **Logic gate synthesis** (AND/OR/XOR operations)

## Problem Summary

Given an n×n binary image, decompose it into rank-1 tensors (outer products of binary vectors) combined with logic gates. Find the minimum number of tensors needed and count all distinct minimal decompositions.

**Challenge**: Understanding tensor decomposition over binary field + gate semantics + combinatorial counting.

## Folder Structure

```
├── qwen/
│   ├── conversations.md     # Qwen test conversation links
│   ├── run_01.py            # Fails: confuses tensor/matrix rank
│   ├── run_02.py            # Fails: wrong counting logic
│   └── run_03.py            # Fails: gate operation bugs
├── test_cases/
│   ├── 1.in / 1.out         # Rank-1 single pixel
│   ├── 2.in / 2.out         # Rank-1 row
│   ├── 3.in / 3.out         # Rank-2 identity
│   ├── 4.in / 4.out         # Zero matrix
│   └── 5.in / 5.out         # Rank-1 block
├── idea.md                  # Problem development process
├── problem.md               # Full problem statement
├── solution.md              # Algorithm explanation
├── solution.py              # Correct DP solution
├── requirements.json        # Time/memory limits
└── README.md                # This file
```

## Solution Approach

1. **Rank-1 check**: Enumerate all (row, col) vector pairs, compute outer products
2. **Rank-2 check**: Try all pairs of rank-1 tensors with AND/OR/XOR gates
3. **Counting**: Track distinct decompositions (different vectors, gates, orderings)

**Complexity**: O(2^(4n) × n²) - feasible for n ≤ 5

## Why This is Hard

- **Tensor concepts**: Outer product r ⊗ c where T[i][j] = r[i] AND c[j]
- **Not matrix rank**: Binary tensor rank ≠ linear algebra rank
- **Gate semantics**: Must verify which gates produce correct result
- **Combinatorics**: Count all valid (vector pair, gate) combinations
- **Edge cases**: Zero matrix (rank 0), identity (rank n)

## Testing

Run test suite:

```bash
python test_runner.py
```

Verify Qwen failures:

```bash
python qwen/run_01.py < test_cases/3.in  # Outputs: 2, 1 (wrong, should be 2, 8)
python qwen/run_02.py < test_cases/3.in  # Outputs: 2, 2 (wrong)
python qwen/run_03.py < test_cases/3.in  # Outputs: 2, 3 (wrong)
python solution.py < test_cases/3.in     # Outputs: 2, 8 (correct)
```

## Qwen Failure Analysis

All three attempts fail because:

1. **run_01.py**: Uses numpy.linalg.matrix_rank (standard linear algebra) instead of binary tensor rank
2. **run_02.py**: Assumes rank = number of set pixels (completely wrong model)
3. **run_03.py**: Uses multiplication instead of AND for outer product, doesn't enumerate decompositions

## Originality

This problem is original because it combines:

- Tensor decomposition over GF(2) (binary field)
- Boolean logic gate synthesis
- Combinatorial counting of equivalent decompositions

Not found on Codeforces, LeetCode, or AtCoder. Requires understanding from multiple domains.

## Requirements

- **Time Limit**: 2 seconds
- **Memory Limit**: 256 MB
- **Constraints**: 1 ≤ n ≤ 5

##License

Educational purposes.
