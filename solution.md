# Solution: Binary Image Tensor Gate Decomposition

## Problem Analysis

Given a binary n×n image, we need to:

1. Find the minimum number of rank-1 tensors required to synthesize it
2. Count the number of distinct minimal decompositions

A rank-1 tensor is the outer product of two binary vectors: T[i][j] = r[i] AND c[j]

## Approach

### Step 1: Check for Rank-1 Matrix

A matrix is rank-1 if it can be expressed as a single outer product.

**Algorithm**:

- Try all possible (r, c) vector pairs (2^n × 2^n possibilities)
- For each pair, compute outer product and compare with target
- Count how many distinct pairs produce the target

**Complexity**: O(2^(2n) × n^2)

### Step 2: Check for Rank-2 Matrix

If not rank-1, try combining two rank-1 tensors with gates.

**Algorithm**:

- Enumerate all possible pairs of rank-1 tensors (T₁, T₂)
- For each pair, try combining with AND, OR, XOR
- Count distinct combinations that produce the target
- Track using set to avoid duplicates

**Complexity**: O(2^(4n) × n^2) - feasible for n ≤ 5

### Step 3: Higher Ranks

For n ≤ 5, almost all matrices have rank ≤ 2. If rank > 2, use worst-case rank = n.

## Key Insights

1. **Rank-1 characterization**: Matrix M is rank-1 iff for all set pixels (i,j) and (k,l), if M[i][l] = M[k][j] = 1, then M[i][j] = M[k][l] = 1 (rectangular structure)

2. **Gate behavior**:

   - OR: Preserves all set pixels from both tensors
   - XOR: Symmetric difference of set pixels
   - AND: Intersection of set pixels

3. **Counting distinct decompositions**:

   - Different (r,c) pairs for same tensor count as different
   - Different gate choices count as different
   - Order matters (T₁ ⊕ T₂ vs T₂ ⊕ T₁ are different for non-commutative operations)

4. **Zero matrix**: Rank 0, exactly 1 decomposition (empty)

## Implementation Details

```python
def find_rank1_decompositions(target):
    # Enumerate all (r,c) pairs
    # Check if outer product equals target
    return list_of_pairs

def count_decompositions(target):
    # Try rank-1
    if rank1_decomps exist:
        return (1, count(rank1_decomps))

    # Try rank-2
    count = 0
    for T1, T2 in all_rank1_tensor_pairs:
        for gate in [AND, OR, XOR]:
            if gate(T1, T2) == target:
                count += 1

    if count > 0:
        return (2, count)

    # Higher rank fallback
    return (n, 1)
```

## Complexity Analysis

- **Time**: O(2^(4n) × n^2) for rank-2 check
- **Space**: O(2^(2n)) for storing tensor combinations
- **Feasible for**: n ≤ 5 (as stated in constraints)

## Edge Cases

1. **Zero matrix**: Rank 0, count = 1
2. **Single pixel**: Rank 1, multiple (r,c) pairs possible
3. **Identity matrix**: Rank n, complex counting
4. **All-ones matrix**: Rank 1
5. **Diagonal matrices**: Usually rank n

## Why AI Models Fail

1. **Misunderstanding outer product**: Confusing with matrix multiplication
2. **Gate semantics**: Not realizing OR/XOR both work for disjoint tensors but give same result
3. **Counting errors**: Double-counting or missing equivalent decompositions
4. **Rank confusion**: Mixing up binary tensor rank with matrix rank
5. **Edge case bugs**: Forgetting zero matrix or single-pixel cases
