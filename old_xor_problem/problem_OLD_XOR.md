# Problem: XOR Balanced Subsequences

## Problem Statement

You are given an array **a** of **n** integers.

A subsequence is called **XOR-balanced** if the XOR of all elements at odd positions (1st, 3rd, 5th, ...) equals the XOR of all elements at even positions (2nd, 4th, 6th, ...) within that subsequence.

**Important**: Positions are counted within the subsequence itself, not in the original array.

For example:

- If we select elements at indices [1, 3, 5] from the array, forming subsequence [a₁, a₃, a₅], then:
  - Odd positions in subsequence: a₁ (1st), a₅ (3rd)
  - Even positions in subsequence: a₃ (2nd)
  - It's XOR-balanced if a₁ ⊕ a₅ = a₃

Count the number of non-empty XOR-balanced subsequences modulo **10⁹ + 7**.

## Input Format

- The first line contains a single integer **n** (1 ≤ n ≤ 3000) — the length of the array.
- The second line contains **n** integers **a₁, a₂, ..., aₙ** (0 ≤ aᵢ ≤ 10⁹) — the elements of the array.

## Output Format

Print a single integer — the number of XOR-balanced subsequences modulo **10⁹ + 7**.

## Examples

### Example 1

**Input:**

```
3
1 2 3
```

**Output:**

```
3
```

**Explanation:**
Let's check all 7 non-empty subsequences:

- [1]: length 1, odd_xor = 1, even_xor = 0 → not balanced
- [2]: length 1, odd_xor = 2, even_xor = 0 → not balanced
- [3]: length 1, odd_xor = 3, even_xor = 0 → not balanced
- [1, 2]: length 2, positions (1,2) → odd_xor = 1, even_xor = 2 → not balanced
- [1, 3]: length 2, positions (1,2) → odd_xor = 1, even_xor = 3 → not balanced
- [2, 3]: length 2, positions (1,2) → odd_xor = 2, even_xor = 3 → not balanced
- [1, 2, 3]: length 3, positions (1,2,3) → odd_xor = 1⊕3 = 2, even_xor = 2 → **balanced** ✓

Only one balanced subsequence: [1, 2, 3].

### Example 2

**Input:**

```
4
0 0 0 0
```

**Output:**

```
15
```

**Explanation:**
Since all elements are 0, XOR is always 0 regardless of which elements we pick. Every subsequence is XOR-balanced (0 ⊕ 0 ⊕ ... = 0). Total non-empty subsequences = 2⁴ - 1 = 15.

### Example 3

**Input:**

```
5
1 1 2 2 3
```

**Output:**

```
11
```

## Notes

- A subsequence with only odd positions (length 1, 3, 5, ...) is XOR-balanced if the XOR of all selected elements equals 0.
- XOR (⊕) is the bitwise exclusive OR operation.
- Remember to take the result modulo 10⁹ + 7.

## Constraints

- 1 ≤ n ≤ 3000
- 0 ≤ aᵢ ≤ 10⁹
- Time limit: 2 seconds
- Memory limit: 256 MB
