# Test Case Generator for XOR Balanced Subsequences

import random
import sys

def generate_test(n, max_val=10**9, seed=None):
    """Generate a test case with n elements"""
    if seed is not None:
        random.seed(seed)
    
    a = [random.randint(0, max_val) for _ in range(n)]
    
    print(n)
    print(' '.join(map(str, a)))

def generate_special_cases():
    """Generate special test cases"""
    
    # All zeros
    print("# Test: All zeros")
    n = 4
    print(n)
    print(' '.join(['0'] * n))
    print()
    
    # All same non-zero
    print("# Test: All same")
    n = 5
    val = 7
    print(n)
    print(' '.join([str(val)] * n))
    print()
    
    # Powers of 2
    print("# Test: Powers of 2")
    powers = [1, 2, 4, 8, 16, 32]
    print(len(powers))
    print(' '.join(map(str, powers)))
    print()
    
    # XOR chain that results in 0
    print("# Test: XOR chain")
    a = [1, 2, 3]  # 1^2^3 = 0
    print(len(a))
    print(' '.join(map(str, a)))
    print()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        seed = int(sys.argv[2]) if len(sys.argv) > 2 else None
        generate_test(n, seed=seed)
    else:
        generate_special_cases()
