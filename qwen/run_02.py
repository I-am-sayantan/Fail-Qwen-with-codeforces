MOD = 10**9 + 7

def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    image = []
    idx = 1
    for i in range(n):
        row = list(map(int, data[idx:idx+n]))
        image.append(row)
        idx += n
        
    target = 0
    for i in range(n):
        for j in range(n):
            if image[i][j]:
                target |= (1 << (i * n + j))
                
    from collections import defaultdict
    dp = [defaultdict(int) for _ in range(n+1)]
    
    total_vec = 1 << n
    for r in range(total_vec):
        for c in range(total_vec):
            mat = 0
            for i in range(n):
                if (r >> i) & 1:
                    for j in range(n):
                        if (c >> j) & 1:
                            mat |= (1 << (i * n + j))
            dp[1][mat] = (dp[1][mat] + 1) % MOD

    if target in dp[1]:
        print(1)
        print(dp[1][target] % MOD)
        return
        
    for k in range(2, n+1):
        for i in range(1, k):
            j = k - i
            for A, cntA in dp[i].items():
                for B, cntB in dp[j].items():
                    total_cnt = (cntA * cntB) % MOD
                    # AND
                    C = A & B
                    dp[k][C] = (dp[k][C] + total_cnt) % MOD
                    # OR
                    C = A | B
                    dp[k][C] = (dp[k][C] + total_cnt) % MOD
                    # XOR
                    C = A ^ B
                    dp[k][C] = (dp[k][C] + total_cnt) % MOD
        if target in dp[k]:
            print(k)
            print(dp[k][target] % MOD)
            return
            
    # Fallback (should not occur)
    print(n)
    print(0)

if __name__ == '__main__':
    main()