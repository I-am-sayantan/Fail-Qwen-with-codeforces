# Solution: XOR Balanced Subsequences

## Problem Analysis

We need to count subsequences where the XOR of elements at odd positions equals the XOR of elements at even positions within the subsequence.

**Key observation**: When building a subsequence element by element, each new element added alternates between going to an odd position and an even position based on the current length of the subsequence.

## Approach: Dynamic Programming

### State Design

We use DP with the following state:

- `dp[i][xor_odd][xor_even][parity]`

Where:

- `i` = current position in array (0 to n-1)
- `xor_odd` = XOR of elements at odd positions in subsequence so far
- `xor_even` = XOR of elements at even positions in subsequence so far
- `parity` = current length of subsequence modulo 2 (0 = even length, 1 = odd length)

**Value**: Number of ways to form such subsequences using first `i` elements.

### Transitions

For each position `i`, we have two choices:

1. **Don't include a[i]**: `dp[i+1][xor_odd][xor_even][parity] += dp[i][xor_odd][xor_even][parity]`

2. **Include a[i]**:

   - If current length is even (parity=0), the next element goes to odd position:
     `dp[i+1][xor_odd ⊕ a[i]][xor_even][1] += dp[i][xor_odd][xor_even][0]`

   - If current length is odd (parity=1), the next element goes to even position:
     `dp[i+1][xor_odd][xor_even ⊕ a[i]][0] += dp[i][xor_odd][xor_even][1]`

### Base Case

- `dp[0][0][0][0] = 1` (empty subsequence with even length)

### Answer Extraction

Count all states where `xor_odd == xor_even` and we have a non-empty subsequence:

- States with parity=0 (even length): both odd_xor and even_xor must be equal
- States with parity=1 (odd length): odd_xor must equal even_xor (even_xor includes implicit 0)

We sum over all positions and all XOR values where odd_xor == even_xor, excluding the empty subsequence.

## Complexity Analysis

- **Time**: O(n × V²) where V is the range of possible XOR values (limited by distinct XORs we encounter)
- **Space**: O(n × V²) or O(V²) with space optimization

Since we only care about XOR values that can actually appear, and n ≤ 3000, we can use a map/dictionary to store only reachable states.

**Optimized complexity**: O(n × S) where S is the number of distinct reachable states, typically much smaller than V².

## Implementation Strategy

Use a dictionary/map to store states instead of a full 4D array:

- Key: (xor_odd, xor_even, parity)
- Value: count of ways

Process elements one by one, maintaining current and next state maps.

## Why Simple Approaches Fail

1. **Brute force enumeration**: 2ⁿ subsequences → too slow for n=3000
2. **Greedy**: No greedy strategy exists for this problem
3. **Simple DP**: Forgetting to track parity leads to wrong position assignments
4. **Misunderstanding positions**: Counting positions in original array vs subsequence

## Edge Cases

- All elements are 0: Every subsequence is balanced
- n = 1: A single element is balanced only if it equals 0
- All elements identical: Multiple balanced subsequences possible
- Large XOR values: Need to use dictionary to avoid memory issues

## Sample Trace (Example 1: [1, 2, 3])

Starting with empty subsequence:

- Add 1 at position 1 (odd): xor_odd=1, xor_even=0, parity=1
- From there, add 2 at position 2 (even): xor_odd=1, xor_even=2, parity=0
- From there, add 3 at position 3 (odd): xor_odd=1⊕3=2, xor_even=2, parity=1
- This gives us a balanced subsequence [1,2,3]

Total balanced subsequences found: 3
