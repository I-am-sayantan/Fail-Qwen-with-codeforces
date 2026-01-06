# Binary Image Tensor Gate Decomposition - Project Repository

## Overview

This repository contains an original competitive programming problem designed to **make Qwen3-235B-A22B-2507 fail**. It combines tensor decomposition (from my IIT bachelor project) with image processing and Boolean gate synthesis.

**Mission Accomplished**: All 3 Qwen attempts fail multiple test cases ✓

## Quick Start

```bash
# Run all tests
python test_runner.py

# Expected output:
# Correct solution: All tests PASS ✓
# run_01.py: FAIL (timeout + wrong answers)
# run_02.py: FAIL (bitmask errors)
# run_03.py: FAIL (counting bugs)
```

## Repository Structure

```
├── problem.md               # Full problem statement (for contestants)
├── idea.md                  # Problem development journey
├── solution.md              # Algorithm explanation
├── solution.py              # ✓ Correct solution (passes 10/10 tests)
├── requirements.json        # Time: 2s, Memory: 256MB
├── test_runner.py           # Automated test suite
│
├── qwen/
│   ├── conversations.md     # Qwen chat links + approaches
│   ├── run_01.py            # ✗ DP state explosion → timeout
│   ├── run_02.py            # ✗ Bitmask logic errors
│   └── run_03.py            # ✗ Incorrect counting
│
├── test_cases/
│   ├── 1-5.in/out           # Original 5 tests
│   └── 6-10.in/out          # Added complex cases
│
└── old_xor_problem/         # Initial attempt (Qwen solved it!)
```

## Solution Visualization

### Example: 2×2 Identity Matrix

```
Input:          Target decomposition:
[1 0]           T₁ = [1,0] ⊗ [1,0]    T₂ = [0,1] ⊗ [0,1]
[0 1]           = [1 0]                = [0 0]
                  [0 0]                  [0 1]

                T₁ OR T₂ = [1 0]  ✓
                           [0 1]

Rank: 2 (need 2 rank-1 tensors)
Count: 8 (4 vector pairs × 1 gate that works × 2 orderings)
```

### Example: 3×3 Checkerboard Pattern

```
Input:          Cannot be expressed as single rank-1 tensor
[1 0 1]         Needs rank ≥ 2
[0 0 0]
[1 0 1]

Solution approach:
1. Enumerate all possible (row, col) vector pairs
2. Compute outer products: M[i][j] = row[i] AND col[j]
3. Try combining pairs with AND/OR/XOR gates
4. Count all distinct minimal decompositions
```

## Test Results Summary

```
════════════════════════════════════════════════════════════════════
BINARY IMAGE TENSOR GATE DECOMPOSITION - TEST RESULTS
════════════════════════════════════════════════════════════════════

✓ solution.py (Correct):     All tests PASSED

✗ qwen/run_01.py:            FAILED - Inefficient DP state enumeration
✗ qwen/run_02.py:            FAILED - Incorrect DP state transitions
✗ qwen/run_03.py:            FAILED - Gate application and counting bugs
════════════════════════════════════════════════════════════════════
```

## Key Insights

**Why This Problem Works**:

- Combines domains AI models don't connect well (tensor algebra + image processing + Boolean circuits)
- Not reducible to known DP patterns
- Requires precise understanding of outer products in binary field
- Edge cases expose conceptual misunderstandings

**From Idea Development** ([idea.md](idea.md)):

- Original XOR problem (by Copilot) → Qwen solved correctly
- Pivoted to tensor decomposition (my IIT bachelor project background)
- Integrated image processing (my research area)
- Result: Genuine multi-domain problem that trips up AI pattern matching

## Originality and Related Work

To ensure this problem is original and not merely a rephrasing of existing problems, extensive research was conducted into related mathematical concepts.

### Related Concepts in Literature

**Boolean Matrix Factorization (BMF)**:

- Standard BMF decomposes a binary matrix as an OR-sum of rank-1 binary matrices
- Equivalent to finding minimum biclique cover in bipartite graphs
- Well-studied in data mining, known to be NP-hard
- Uses **only OR** operation for combining factors

**XOR-based Decomposition (GF(2) Rank)**:

- Decomposes as XOR-sum of rank-1 factors (e.g., XBMaD algorithm)
- Each 1 in matrix covered odd number of times, each 0 even times
- Used in communication complexity and data compression
- Uses **only XOR** operation for combining factors

**Biclique Cover/Partition**:

- Minimum number of complete bipartite subgraphs covering all 1-entries
- Binary rank over GF(2) with disjoint decomposition
- Appears in graph theory and communication complexity

### Key Distinction: Why This Problem Is Novel

**None of the existing literature combines AND/OR/XOR gates together**:

1. **Standard BMF**: Uses only OR (monotonic combination, can only add 1's)
2. **XOR models**: Uses only XOR (exact coverage, parity-based)
3. **This problem**: Allows AND, OR, and XOR gates simultaneously

**Critical difference with AND gate**:

- AND can **remove** 1's (intersection of patterns)
- This is fundamentally different from OR/XOR which are additive
- No prior work explicitly combines all three Boolean gates for decomposition

**Example demonstrating uniqueness**:

```
Matrix: [1 0]
        [0 0]

OR-only:   Can express as single rank-1 tensor
XOR-only:  Can express as single rank-1 tensor
AND-only:  Can express as single rank-1 tensor

But allowing AND+OR+XOR together:
- Creates multiple valid decomposition paths
- Counting becomes combinatorially complex
- Must verify which gate combinations actually work
```

### Literature Consulted

- Boolean matrix factorization algorithms and complexity (ScienceDirect, Math StackExchange)
- XOR-rank and GF(2) decomposition (arXiv, WickerLab publications)
- Biclique cover problems in graph theory
- Communication complexity and Boolean rank

### Conclusion on Originality

**This problem is NOT a rephrasing** because:

- It extends standard boolean decomposition by allowing AND gates
- Existing work treats OR and XOR separately, never combined with AND
- The specific formulation (rank-1 outer products + all three gates + count decompositions) is novel
- No identical or closely similar problem found in competitive programming or academic literature

**It builds on known concepts** (Boolean factorization, tensor decomposition) **but creates a genuinely new problem** by combining operations in an unstudied way.

## Documentation

- **[problem.md](problem.md)** - Full problem statement for contestants
- **[idea.md](idea.md)** - Journey from XOR problem to tensor decomposition
- **[solution.md](solution.md)** - Algorithm explanation with examples
- **[qwen/conversations.md](qwen/conversations.md)** - Qwen chat links and failure analysis

## License

Educational purposes - Demonstrating AI model limitations on multi-domain problems.
