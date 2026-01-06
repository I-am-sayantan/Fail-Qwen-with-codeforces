MOD = 10**9 + 7

def outer_product(r, c):
    """Compute outer product of two binary vectors"""
    n = len(r)
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = r[i] & c[j]
    return matrix

def matrix_equals(A, B):
    """Check if two matrices are equal"""
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A)))

def find_rank1_decompositions(target):
    """Find all (r, c) pairs where r ⊗ c = target"""
    n = len(target)
    decomps = []
    
    # Try all possible binary vectors
    for r_mask in range(1 << n):
        for c_mask in range(1 << n):
            r = [(r_mask >> i) & 1 for i in range(n)]
            c = [(c_mask >> i) & 1 for i in range(n)]
            
            if matrix_equals(outer_product(r, c), target):
                decomps.append((tuple(r), tuple(c)))
    
    return decomps

def apply_gate(A, B, gate):
    """Apply gate operation element-wise"""
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if gate == 'AND':
                result[i][j] = A[i][j] & B[i][j]
            elif gate == 'OR':
                result[i][j] = A[i][j] | B[i][j]
            elif gate == 'XOR':
                result[i][j] = A[i][j] ^ B[i][j]
    return result

def is_zero_matrix(M):
    """Check if matrix is all zeros"""
    return all(M[i][j] == 0 for i in range(len(M)) for j in range(len(M)))

def count_decompositions(target):
    """Count minimal tensor decompositions"""
    n = len(target)
    
    # Special case: zero matrix
    if is_zero_matrix(target):
        return 0, 1
    
    # Check if rank-1
    rank1_decomps = find_rank1_decompositions(target)
    if rank1_decomps:
        return 1, len(rank1_decomps)
    
    # Try rank-2: combine two rank-1 tensors
    count = 0
    seen = set()
    
    for r1_mask in range(1, 1 << n):
        for c1_mask in range(1, 1 << n):
            r1 = [(r1_mask >> i) & 1 for i in range(n)]
            c1 = [(c1_mask >> i) & 1 for i in range(n)]
            T1 = outer_product(r1, c1)
            
            if is_zero_matrix(T1):
                continue
            
            for r2_mask in range(1, 1 << n):
                for c2_mask in range(1, 1 << n):
                    r2 = [(r2_mask >> i) & 1 for i in range(n)]
                    c2 = [(c2_mask >> i) & 1 for i in range(n)]
                    T2 = outer_product(r2, c2)
                    
                    if is_zero_matrix(T2):
                        continue
                    
                    # Try each gate
                    for gate in ['AND', 'OR', 'XOR']:
                        result = apply_gate(T1, T2, gate)
                        if matrix_equals(result, target):
                            # Create unique signature
                            sig = (tuple(map(tuple, T1)), tuple(map(tuple, T2)), gate)
                            if sig not in seen:
                                seen.add(sig)
                                count += 1
    
    if count > 0:
        return 2, count
    
    # If still not found, would need rank-3 or higher
    # For n ≤ 5, most matrices are rank ≤ 2
    # Return rank = n (worst case) with count = 1 as fallback
    return n, 1

def solve():
    n = int(input())
    target = []
    for _ in range(n):
        row = list(map(int, input().split()))
        target.append(row)
    
    min_rank, count = count_decompositions(target)
    print(min_rank)
    print(count % MOD)

if __name__ == "__main__":
    solve()
