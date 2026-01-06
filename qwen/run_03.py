MOD = 10**9 + 7

def main():
    import sys
    from collections import defaultdict
    data = sys.stdin.read().split()
    n = int(data[0])
    matrix = []
    index = 1
    for i in range(n):
        row = list(map(int, data[index:index + n]))
        matrix.append(row)
        index += n
    
    target_mask = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                bit_pos = i * n + j
                target_mask |= (1 << bit_pos)
    
    if n == 0:
        print(0)
        print(1)
        return
        
    total_r = 1 << n
    count1 = defaultdict(int)
    
    for r in range(total_r):
        for c in range(total_r):
            tensor_mask = 0
            for i in range(n):
                if (r >> i) & 1:
                    for j in range(n):
                        if (c >> j) & 1:
                            bit_pos = i * n + j
                            tensor_mask |= (1 << bit_pos)
            count1[tensor_mask] += 1

    if target_mask == 0:
        print(1)
        print(count1[0] % MOD)
        return

    dp = []
    dp1 = defaultdict(int)
    for mask, cnt in count1.items():
        dp1[mask] = cnt % MOD
    dp.append(dp1)
    
    if target_mask in dp1:
        print(1)
        print(dp1[target_mask] % MOD)
        return
        
    max_k = n * n
    for k_val in range(2, max_k + 1):
        dpk = defaultdict(int)
        for i in range(1, k_val):
            j = k_val - i
            left_dict = dp[i - 1]
            right_dict = dp[j - 1]
            for left_mask, left_count in left_dict.items():
                for right_mask, right_count in right_dict.items():
                    prod = (left_count * right_count) % MOD
                    
                    and_res = left_mask & right_mask
                    dpk[and_res] = (dpk[and_res] + prod) % MOD
                    
                    or_res = left_mask | right_mask
                    dpk[or_res] = (dpk[or_res] + prod) % MOD
                    
                    xor_res = left_mask ^ right_mask
                    dpk[xor_res] = (dpk[xor_res] + prod) % MOD
                    
        if target_mask in dpk:
            print(k_val)
            print(dpk[target_mask] % MOD)
            return
            
        dp.append(dpk)
    
    print(max_k)
    print(dp[max_k - 1].get(target_mask, 0) % MOD)

if __name__ == "__main__":
    main()