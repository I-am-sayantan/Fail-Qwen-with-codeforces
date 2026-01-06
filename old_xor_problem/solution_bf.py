# Optional: Brute Force Solution for Testing

# This solution enumerates all possible subsequences and checks each one
# Time complexity: O(2^n * n) - only works for small n

MOD = 10**9 + 7

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    count = 0
    
    # Enumerate all non-empty subsequences
    for mask in range(1, 1 << n):
        subsequence = []
        
        for i in range(n):
            if mask & (1 << i):
                subsequence.append(a[i])
        
        # Calculate XOR at odd and even positions WITHIN the subsequence
        xor_odd = 0
        xor_even = 0
        
        for pos in range(len(subsequence)):
            if pos % 2 == 0:  # Position 0, 2, 4, ... (1st, 3rd, 5th in 1-indexed)
                xor_odd ^= subsequence[pos]
            else:  # Position 1, 3, 5, ... (2nd, 4th, 6th in 1-indexed)
                xor_even ^= subsequence[pos]
        
        if xor_odd == xor_even:
            count += 1
    
    print(count % MOD)

if __name__ == "__main__":
    solve()
