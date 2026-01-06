#!/usr/bin/env python3
"""
Test Runner for Binary Image Tensor Gate Decomposition Problem
Runs the correct solution and Qwen attempts against all test cases
"""

import subprocess
import sys
import os
from pathlib import Path

def run_solution(script_path, input_file):
    """Run a solution script with the given input file"""
    try:
        with open(input_file, 'r') as f:
            result = subprocess.run(
                ['python', script_path],
                stdin=f,
                capture_output=True,
                text=True,
                timeout=5
            )
        return result.stdout.strip(), result.returncode
    except subprocess.TimeoutExpired:
        return "TIMEOUT", -1
    except Exception as e:
        return f"ERROR: {str(e)}", -1

def compare_output(actual, expected):
    """Compare actual output with expected output"""
    actual_lines = actual.strip().split('\n')
    expected_lines = expected.strip().split('\n')
    
    if len(actual_lines) != len(expected_lines):
        return False
    
    for a, e in zip(actual_lines, expected_lines):
        if a.strip() != e.strip():
            return False
    
    return True

def main():
    # Find all test cases
    test_dir = Path("test_cases")
    test_numbers = sorted(set(
        int(f.stem) for f in test_dir.glob("*.in")
    ))
    
    print("="*80)
    print("BINARY IMAGE TENSOR GATE DECOMPOSITION - TEST RUNNER")
    print("="*80)
    
    # Test correct solution
    print("\n1. CORRECT SOLUTION (solution.py):")
    print("-"*80)
    
    correct_passes = 0
    for test_num in test_numbers:
        input_file = test_dir / f"{test_num}.in"
        output_file = test_dir / f"{test_num}.out"
        
        with open(output_file, 'r') as f:
            expected = f.read().strip()
        
        actual, rc = run_solution("solution.py", input_file)
        
        if compare_output(actual, expected):
            print(f"  Test {test_num}: ✓ PASS")
            correct_passes += 1
        else:
            print(f"  Test {test_num}: ✗ FAIL")
            print(f"    Expected: {expected}")
            print(f"    Got:      {actual}")
    
    total_tests = len(test_numbers)
    print(f"\nResult: {correct_passes}/{total_tests} tests passed")
    
    # Test Qwen solutions
    print("\n2. QWEN SOLUTIONS (should fail some tests):")
    print("-"*80)
    
    qwen_scripts = ["qwen/run_01.py", "qwen/run_02.py", "qwen/run_03.py"]
    
    for script in qwen_scripts:
        if not os.path.exists(script):
            print(f"\n  {script}: NOT FOUND (skipping)")
            continue
            
        print(f"\n  {script}:")
        
        failures = 0
        for test_num in test_numbers:
            input_file = test_dir / f"{test_num}.in"
            output_file = test_dir / f"{test_num}.out"
            
            with open(output_file, 'r') as f:
                expected = f.read().strip()
            
            actual, rc = run_solution(script, input_file)
            
            if compare_output(actual, expected):
                print(f"    Test {test_num}: PASS (expected: {expected})")
            else:
                failures += 1
                print(f"    Test {test_num}: ✗ FAIL (expected: {expected}, got: {actual})")
        
        print(f"  {script}: {failures}/{total_tests} tests failed")
    
    # Summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"✓ Total test cases: {total_tests}")
    print(f"✓ Correct solution: {correct_passes}/{total_tests} passed")
    print("="*80)

if __name__ == "__main__":
    main()
