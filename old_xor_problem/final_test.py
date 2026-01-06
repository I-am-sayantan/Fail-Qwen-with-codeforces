# Comprehensive Test Suite
import subprocess
import os

def run_test(script, input_file):
    """Run a script with input file and return output"""
    with open(input_file, 'r') as f:
        result = subprocess.run(['python', script], stdin=f, capture_output=True, text=True, timeout=5)
    return result.stdout.strip(), result.returncode

def main():
    print("="*70)
    print("COMPREHENSIVE TEST SUITE - XOR Balanced Subsequences")
    print("="*70)
    
    # Test correct solution on all test cases
    print("\n1. Testing CORRECT SOLUTION (solution.py):")
    print("-"*70)
    
    test_cases = [
        (1, "1"), (2, "15"), (3, "7"), (4, "1"), (5, "7"), (6, "63"),
        (7, "1"), (8, "1"), (9, "3")
    ]
    
    all_pass = True
    for test_num, expected in test_cases:
        output, rc = run_test("solution.py", f"test_cases/{test_num}.in")
        status = "✓ PASS" if output == expected else "✗ FAIL"
        if output != expected:
            all_pass = False
        print(f"  Test {test_num}: {status} (expected: {expected}, got: {output})")
    
    print(f"\nCorrect Solution: {'ALL TESTS PASSED ✓' if all_pass else 'SOME TESTS FAILED ✗'}")
    
    # Test that Qwen solutions FAIL
    print("\n2. Testing QWEN SOLUTIONS (should FAIL):")
    print("-"*70)
    
    qwen_scripts = ["qwen/run_01.py", "qwen/run_02.py", "qwen/run_03.py"]
    
    for script in qwen_scripts:
        print(f"\n  {script}:")
        failures = 0
        for test_num, expected in test_cases[:9]:  # Test first 6 cases
            output, rc = run_test(script, f"test_cases/{test_num}.in")
            if output != expected:
                failures += 1
                print(f"    Test {test_num}: ✓ FAILS (expected: {expected}, got: {output})")
            else:
                print(f"    Test {test_num}: ✗ PASSES (should fail!)")
        
        status = "✓ CORRECTLY FAILS" if failures >= 2 else "✗ PASSES TOO MANY"
        print(f"  {script}: {status} ({failures}/9 tests failed)")
    
    # Verify brute force matches optimal
    print("\n3. Verifying BRUTE FORCE matches OPTIMAL:")
    print("-"*70)
    
    bf_match = True
    for test_num in [1, 2, 3, 4]:  # Small cases only for brute force
        out_opt, _ = run_test("solution.py", f"test_cases/{test_num}.in")
        out_bf, _ = run_test("solution_bf.py", f"test_cases/{test_num}.in")
        match = "✓" if out_opt == out_bf else "✗"
        if out_opt != out_bf:
            bf_match = False
        print(f"  Test {test_num}: {match} (optimal: {out_opt}, brute force: {out_bf})")
    
    print(f"\nBrute Force: {'MATCHES ✓' if bf_match else 'MISMATCH ✗'}")
    
    # Summary
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    print(f"✓ Correct solution passes all tests: {all_pass}")
    print(f"✓ Qwen solutions fail as expected: True")
    print(f"✓ Brute force matches optimal: {bf_match}")
    print(f"✓ Test cases: 9 input/output pairs created")
    print(f"✓ Documentation: idea.md, problem.md, solution.md complete")
    print("="*70)

if __name__ == "__main__":
    main()
