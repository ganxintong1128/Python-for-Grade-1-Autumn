import time
import random
import math

def find_prime_trial_division(n):
    """Method 1: Basic Trial Division"""
    time_start = time.time()
    number_pn = 0
    
    def is_prime(num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                return False
        return True
    
    for i in range(2, n + 1):
        if is_prime(i):
            number_pn += 1
    
    time_end = time.time()
    return time_end - time_start, number_pn

def find_prime_sieve_eratosthenes(n):
    """Method 2: Sieve of Eratosthenes"""
    time_start = time.time()
    
    if n < 2:
        return 0, 0
    
    # Create a boolean array and initialize all entries as true
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    
    p = 2
    while p * p <= n:
        if prime[p]:
            # Update all multiples of p starting from p*p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    
    # Count primes
    number_pn = sum(prime)
    
    time_end = time.time()
    return time_end - time_start, number_pn

def find_prime_optimized_sieve(n):
    """Method 3: Optimized Sieve (6k±1 optimization)"""
    time_start = time.time()
    
    if n < 2:
        return 0, 0
    if n < 3:
        return time.time() - time_start, 1
    
    # Handle 2 and 3 separately
    prime = [False] * (n + 1)
    prime[2] = prime[3] = True
    
    # Only check numbers of the form 6k±1
    for i in range(5, n + 1, 6):
        if i <= n:
            prime[i] = True
        if i + 2 <= n:
            prime[i + 2] = True
    
    # Sieve
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False
        if i + 2 <= int(math.sqrt(n)) + 1 and prime[i + 2]:
            for j in range((i + 2) * (i + 2), n + 1, i + 2):
                prime[j] = False
    
    number_pn = sum(prime)
    
    time_end = time.time()
    return time_end - time_start, number_pn

def find_prime_segmented_sieve(n):
    """Method 4: Segmented Sieve"""
    time_start = time.time()
    
    if n < 2:
        return 0, 0
    
    # First find all primes up to sqrt(n) using simple sieve
    limit = int(math.sqrt(n)) + 1
    prime = [True] * limit
    prime[0] = prime[1] = False
    
    for i in range(2, int(math.sqrt(limit)) + 1):
        if prime[i]:
            for j in range(i * i, limit, i):
                prime[j] = False
    
    # Store all primes up to sqrt(n)
    primes = [i for i in range(2, limit) if prime[i]]
    
    # Count primes up to sqrt(n)
    number_pn = len([p for p in primes if p <= n])
    
    # Process segments
    segment_size = max(int(math.sqrt(n)), 32768)
    
    for low in range(limit, n + 1, segment_size):
        high = min(low + segment_size - 1, n)
        
        # Create a boolean array for current segment
        segment = [True] * (high - low + 1)
        
        # Mark multiples of primes in current segment
        for prime_num in primes:
            # Find the minimum number in [low, high] that is a multiple of prime_num
            start = max(prime_num * prime_num, (low + prime_num - 1) // prime_num * prime_num)
            
            # Mark multiples of prime_num in current segment
            for j in range(start, high + 1, prime_num):
                segment[j - low] = False
        
        # Count primes in current segment
        for i in range(len(segment)):
            if segment[i]:
                number_pn += 1
    
    time_end = time.time()
    return time_end - time_start, number_pn

def find_prime_miller_rabin(n):
    """Method 5: Miller-Rabin Primality Test"""
    time_start = time.time()
    number_pn = 0
    
    def mod_pow(base, exp, mod):
        """Fast modular exponentiation"""
        result = 1
        base = base % mod
        while exp > 0:
            if exp % 2 == 1:
                result = (result * base) % mod
            base = (base * base) % mod
            exp = exp // 2
        return result
    
    def miller_rabin_test(n, a):
        """Miller-Rabin test for a specific base a"""
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0:
            return False
        
        # Write n-1 as u * 2^t
        u = n - 1
        t = 0
        while u % 2 == 0:
            u //= 2
            t += 1
        
        # Compute a^u mod n
        y = mod_pow(a, u, n)
        
        # If a^u ≡ 1 (mod n) or a^u ≡ -1 (mod n), then n passes the test for base a
        if y == 1 or y == n - 1:
            return True
        
        # Square y repeatedly t-1 times
        for _ in range(t - 1):
            y = mod_pow(y, 2, n)
            if y == n - 1:
                return True
            if y == 1:
                return False
        
        return False
    
    def is_prime_miller_rabin(num):
        """Check if number is prime using Miller-Rabin test"""
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0:
            return False
        
        # For numbers up to certain limits, these bases are sufficient
        if num < 2047:
            test_bases = [2]
        elif num < 1373653:
            test_bases = [2, 3]
        elif num < 9080191:
            test_bases = [31, 73]
        elif num < 25326001:
            test_bases = [2, 3, 5]
        elif num < 3215031751:
            test_bases = [2, 3, 5, 7]
        elif num < 4759123141:
            test_bases = [2, 7, 61]
        elif num < 1122004669633:
            test_bases = [2, 13, 23, 1662803]
        elif num < 2152302898747:
            test_bases = [2, 3, 5, 7, 11]
        elif num < 3474749660383:
            test_bases = [2, 3, 5, 7, 11, 13]
        elif num < 341550071728321:
            test_bases = [2, 3, 5, 7, 11, 13, 17]
        else:
            # For very large numbers, use first few primes
            test_bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
        
        # Test with all bases
        for a in test_bases:
            if a >= num:
                continue
            if not miller_rabin_test(num, a):
                return False
        
        return True
    
    # Count primes using Miller-Rabin test
    for i in range(2, n + 1):
        if is_prime_miller_rabin(i):
            number_pn += 1
    
    time_end = time.time()
    return time_end - time_start, number_pn

def test_large_primes():
    """Test the Miller-Rabin implementation with large known primes"""
    print("\n" + "="*60)
    print("TESTING LARGE PRIME NUMBERS")
    print("="*60)
    
    def is_prime_miller_rabin_single(num):
        """Single number Miller-Rabin test"""
        def mod_pow(base, exp, mod):
            result = 1
            base = base % mod
            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % mod
                base = (base * base) % mod
                exp = exp // 2
            return result
        
        def miller_rabin_test(n, a):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0:
                return False
            
            u = n - 1
            t = 0
            while u % 2 == 0:
                u //= 2
                t += 1
            
            y = mod_pow(a, u, n)
            
            if y == 1 or y == n - 1:
                return True
            
            for _ in range(t - 1):
                y = mod_pow(y, 2, n)
                if y == n - 1:
                    return True
                if y == 1:
                    return False
            
            return False
        
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0:
            return False
        
        # Use sufficient bases for large numbers
        test_bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        
        for a in test_bases:
            if a >= num:
                continue
            if not miller_rabin_test(num, a):
                return False
        
        return True
    
    # Test cases from the problem
    large_primes = [
        1000000000000037,
        909091,
        99990001,
        999999000001,
        9999999900000001,
        909090909090909091,
        1111111111111111111,
        11111111111111111111111,
        900900900900990990990991
    ]
    
    print(f"{'Number':<25} {'Is Prime':<10} {'Time (ms)':<12}")
    print("-" * 50)
    
    for num in large_primes:
        start_time = time.time()
        is_prime = is_prime_miller_rabin_single(num)
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
        
        print(f"{num:<25} {is_prime:<10} {execution_time:<12.4f}")

def main():
    """Main function to test all methods"""
    print("PRIME NUMBER ALGORITHMS COMPARISON")
    print("="*60)
    print("Finding prime numbers less than 1,000,000")
    print("="*60)
    
    n = 1000000
    methods = [
        ("Trial Division", find_prime_trial_division),
        ("Sieve of Eratosthenes", find_prime_sieve_eratosthenes),
        ("Optimized Sieve", find_prime_optimized_sieve),
        ("Segmented Sieve", find_prime_segmented_sieve),
        ("Miller-Rabin", find_prime_miller_rabin)
    ]
    
    results = []
    
    print(f"{'Method':<25} {'Time (s)':<12} {'Count':<10} {'Correct':<10}")
    print("-" * 60)
    
    expected_count = None
    
    for name, method in methods:
        try:
            if name == "Miller-Rabin":
                # For Miller-Rabin, test with smaller n first due to time complexity
                print(f"\nTesting {name} with smaller range (n=100,000)...")
                exec_time, count = method(100000)
                print(f"{name:<25} {exec_time:<12.4f} {count:<10} {'N/A':<10}")
                continue
            
            exec_time, count = method(n)
            
            if expected_count is None:
                expected_count = count
            
            is_correct = "Yes" if count == expected_count else "No"
            results.append((name, exec_time, count, is_correct))
            
            print(f"{name:<25} {exec_time:<12.4f} {count:<10} {is_correct:<10}")
            
        except Exception as e:
            print(f"{name:<25} {'ERROR':<12} {'N/A':<10} {'No':<10}")
            print(f"Error: {e}")
    
    # Test with smaller numbers for verification
    print("\n" + "="*60)
    print("VERIFICATION WITH SMALLER NUMBERS")
    print("="*60)
    
    test_n = 10000
    print(f"Testing with n = {test_n}")
    print(f"{'Method':<25} {'Time (s)':<12} {'Count':<10}")
    print("-" * 50)
    
    for name, method in methods:
        try:
            exec_time, count = method(test_n)
            print(f"{name:<25} {exec_time:<12.4f} {count:<10}")
        except Exception as e:
            print(f"{name:<25} {'ERROR':<12} {'N/A':<10}")
    
    # Test large primes
    test_large_primes()

if __name__ == "__main__":
    main()
