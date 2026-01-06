MOD = 10**9 + 7

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    # dp[xor_odd][xor_even][parity] = count
    # parity: 0 = even length, 1 = odd length
    dp = {}
    dp[(0, 0, 0)] = 1  # empty subsequence with even length
    
    for num in a:
        new_dp = {}
        
        for (xor_odd, xor_even, parity), count in dp.items():
            # Don't include current number
            key = (xor_odd, xor_even, parity)
            new_dp[key] = (new_dp.get(key, 0) + count) % MOD
            
            # Include current number
            if parity == 0:  # even length -> add to odd position
                key = (xor_odd ^ num, xor_even, 1)
                new_dp[key] = (new_dp.get(key, 0) + count) % MOD
            else:  # odd length -> add to even position
                key = (xor_odd, xor_even ^ num, 0)
                new_dp[key] = (new_dp.get(key, 0) + count) % MOD
        
        dp = new_dp
    
    # Count balanced subsequences (where xor_odd == xor_even)
    result = 0
    for (xor_odd, xor_even, parity), count in dp.items():
        if xor_odd == xor_even:
            result = (result + count) % MOD
    
    # Subtract 1 for the empty subsequence
    result = (result - 1 + MOD) % MOD
    
    print(result)

if __name__ == "__main__":
    solve()
