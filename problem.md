# Problem: Binary Image Tensor Gate Decomposition

## Problem Statement

You are given an **n × n binary image** (matrix where each pixel is 0 or 1).

A **rank-1 tensor** is a binary matrix formed by the outer product of two binary vectors:

- Given row vector **r** = [r₁, r₂, ..., rₙ] and column vector **c** = [c₁, c₂, ..., cₙ]
- The rank-1 tensor T[i][j] = r[i] AND c[j]
- Example: r=[1,0,1], c=[1,1,0] gives T = [[1,1,0],[0,0,0],[1,1,0]]

You can **synthesize** the target image by:

1. Creating rank-1 tensors from binary vectors
2. Combining them using **gate operations**:
   - **AND**: R[i][j] = A[i][j] AND B[i][j]
   - **OR**: R[i][j] = A[i][j] OR B[i][j]
   - **XOR**: R[i][j] = A[i][j] XOR B[i][j]

**Goal**: Find the minimum number of rank-1 tensors needed to synthesize the target image.

**Count**: How many different minimal decompositions exist, modulo **10⁹ + 7**.

Two decompositions are different if they use:

- Different sets of rank-1 tensors (different row/column vector pairs)
- Different gate operations at any combination step
- Different ordering of operations

## Input Format

- First line: one integer **n** (1 ≤ n ≤ 5)
- Next n lines: n space-separated binary digits (0 or 1) representing the image

## Output Format

Two integers on separate lines:

1. Minimum number of rank-1 tensors needed
2. Number of distinct minimal decompositions modulo 10⁹ + 7

## Examples

### Example 1

**Input:**

```
2
1 0
0 0
```

**Output:**

```
1
1
```

**Explanation:**
The image [[1,0],[0,0]] is already a rank-1 tensor.

- r = [1,0], c = [1,0]
- Outer product: [[1,0],[0,0]] ✓
  Only 1 decomposition exists.

### Example 2

**Input:**

```
2
1 1
0 0
```

**Output:**

```
1
2
```

**Explanation:**
Rank-1: r=[1,0], c=[1,1] gives [[1,1],[0,0]].
Two different vector pairs produce this matrix.

### Example 3

**Input:**

```
2
1 0
0 1
```

**Output:**

```
2
4
```

**Explanation:**
Identity matrix requires 2 rank-1 tensors.

- T₁: r₁=[1,0], c₁=[1,0] → [[1,0],[0,0]]
- T₂: r₂=[0,1], c₂=[0,1] → [[0,0],[0,1]]
- Combine with OR or XOR (both work)
- Multiple ways to choose vectors and gates → 4 total

## Constraints

- 1 ≤ n ≤ 5
- Each pixel is 0 or 1
- Time limit: 2 seconds
- Memory limit: 256 MB

## Notes

- **Tensor rank** of a binary matrix is the minimum number of rank-1 tensors needed
- For rank-1 matrices: only 1 tensor needed, but multiple vector pairs may exist
- For higher rank: need to combine multiple tensors with gates
- OR and XOR preserve pixel unions (set pixels remain set)
- AND can eliminate pixels
- This combines tensor decomposition theory with Boolean circuit synthesis
