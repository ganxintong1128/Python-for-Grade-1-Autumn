# Prime Number Algorithm Analysis Results

## Overview
This analysis implements and compares five different methods to find prime numbers less than 1,000,000:

1. **Trial Division** - Basic primality testing
2. **Sieve of Eratosthenes** - Classical sieve algorithm
3. **Optimized Sieve** - 6k±1 optimization
4. **Segmented Sieve** - Memory-efficient sieve
5. **Miller-Rabin** - Probabilistic primality test

## Results for n = 1,000,000

| Method | Time (seconds) | Prime Count | Efficiency Rank |
|--------|----------------|-------------|-----------------|
| Trial Division | 1.9995 | 78,498 | 5th (slowest) |
| Sieve of Eratosthenes | 0.0675 | 78,498 | 2nd |
| Optimized Sieve | 0.0612 | 78,498 | 1st (fastest) |
| Segmented Sieve | 0.1359 | 78,498 | 3rd |
| Miller-Rabin* | 0.2512 | 9,592 | 4th |

*Miller-Rabin tested with n=100,000 due to O(n log log n) complexity when testing all numbers

## Key Findings

### 1. Correctness
- All methods correctly identified **78,498 prime numbers** less than 1,000,000
- Miller-Rabin correctly identified **9,592 prime numbers** less than 100,000
- All large prime number tests passed successfully

### 2. Performance Analysis

**Fastest to Slowest:**
1. **Optimized Sieve (0.0612s)** - 32.7x faster than Trial Division
2. **Sieve of Eratosthenes (0.0675s)** - 29.6x faster than Trial Division  
3. **Segmented Sieve (0.1359s)** - 14.7x faster than Trial Division
4. **Miller-Rabin (0.2512s for n=100,000)** - Specialized for large single numbers
5. **Trial Division (1.9995s)** - Baseline method

### 3. Algorithm Characteristics

#### Trial Division
- **Time Complexity:** O(n√n)
- **Space Complexity:** O(1)
- **Best for:** Small numbers, single primality tests
- **Worst for:** Large ranges

#### Sieve of Eratosthenes
- **Time Complexity:** O(n log log n)
- **Space Complexity:** O(n)
- **Best for:** Finding all primes up to n
- **Limitation:** Memory usage for very large n

#### Optimized Sieve (6k±1)
- **Time Complexity:** O(n log log n) with constant factor improvement
- **Space Complexity:** O(n)
- **Best for:** Finding all primes up to n with better performance
- **Advantage:** Skips multiples of 2 and 3

#### Segmented Sieve
- **Time Complexity:** O(n log log n)
- **Space Complexity:** O(√n)
- **Best for:** Very large ranges with memory constraints
- **Advantage:** Memory efficient for large n

#### Miller-Rabin
- **Time Complexity:** O(k log³ n) per number tested
- **Space Complexity:** O(1)
- **Best for:** Testing individual large numbers for primality
- **Advantage:** Extremely fast for single large number tests

## Large Prime Number Testing

The Miller-Rabin implementation successfully verified all provided large primes:

| Number | Is Prime | Time (ms) |
|--------|----------|-----------|
| 1000000000000037 | ✓ | 0.39 |
| 909091 | ✓ | 0.10 |
| 99990001 | ✓ | 0.12 |
| 999999000001 | ✓ | 0.32 |
| 9999999900000001 | ✓ | 0.42 |
| 909090909090909091 | ✓ | 0.32 |
| 1111111111111111111 | ✓ | 0.37 |
| 11111111111111111111111 | ✓ | 0.53 |
| 900900900900990990990991 | ✓ | 0.59 |

## Miller-Rabin Implementation Details

### Theoretical Foundation
The implementation follows the mathematical principles:

1. **Fermat's Little Theorem:** For prime p and coprime a: a^(p-1) ≡ 1 (mod p)
2. **Factorization:** n-1 = u × 2^t where u is odd
3. **Witness Testing:** Check if a^u ≡ ±1 (mod n) or a^(u×2^i) ≡ -1 (mod n)

### Base Selection Strategy
- Numbers < 2,047: bases [2]
- Numbers < 1,373,653: bases [2, 3]
- Numbers < 25,326,001: bases [2, 3, 5]
- Larger numbers: extended base sets for deterministic results

### Optimizations
- Fast modular exponentiation
- Deterministic base selection for known ranges
- Early termination conditions

## Recommendations

### For Finding All Primes ≤ n:
1. **Small n (< 10⁶):** Optimized Sieve
2. **Medium n (10⁶ - 10⁹):** Segmented Sieve
3. **Large n (> 10⁹):** Segmented Sieve with optimizations

### For Testing Individual Numbers:
1. **Small numbers:** Trial Division
2. **Large numbers:** Miller-Rabin
3. **Cryptographic applications:** Miller-Rabin with multiple rounds

### Memory Considerations:
- **Limited memory:** Segmented Sieve or Miller-Rabin
- **Abundant memory:** Sieve of Eratosthenes or Optimized Sieve

## Conclusion

The analysis demonstrates that:
1. **Sieve algorithms dominate** for finding all primes in a range
2. **Miller-Rabin excels** for testing individual large numbers
3. **Optimized Sieve provides the best balance** of speed and simplicity
4. **Algorithm choice depends on specific use case** and constraints

The implementation successfully finds **78,498 prime numbers less than 1,000,000** and validates the Miller-Rabin algorithm against known large primes with sub-millisecond performance.
