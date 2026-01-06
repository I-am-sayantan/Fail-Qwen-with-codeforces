# SIMPLIFIED PROBLEM: Binary Image Row-Column XOR

## Problem Statement

You are given an **n × m** binary image (matrix of 0s and 1s).

You can perform two types of operations:

1. **Row XOR**: Pick a row i, XOR it with any binary pattern of length m
2. **Column XOR**: Pick a column j, XOR it with any binary pattern of length n

**Goal**: Transform the image to all zeros using the **minimum number of operations**.

Count how many different **minimal operation sequences** achieve this, modulo 10⁹ + 7.

Two sequences are different if they differ in:

- The order of operations
- Which rows/columns are modified
- The XOR patterns used

## Why This is Hard

- Looks simple but order matters
- Some sequences may not lead to all zeros
- Must find minimum first, then count sequences
- Interaction between row and column operations creates dependencies

This should fail AI models that don't properly track dependencies!

Would you like me to develop this simpler version instead? It's:
✅ Still image-based
✅ Uses XOR (gate-like operation)
✅ Has counting complexity
✅ Much clearer to state and solve
✅ Will still trip up AI models
