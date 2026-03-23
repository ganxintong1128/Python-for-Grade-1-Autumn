import time

# Your Miller-Rabin implementation
def find_prime_miller_rabin(n):
    time_start = time.time()
    number_pn = 0
    
    def mod_pow(base, exp, mod):
        result = 1
        base = base % mod
        while exp > 0:
            if exp % 2 == 1:
                result = (result * base) % mod
            base = (base * base) % mod
            exp = exp // 2
        return result

    def is_prime(x):
        if x == 2 or x == 3:
            return True
        elif x % 2 == 0:
            return False
    
        u = x - 1
        t = 0
        while u % 2 == 0:
            u //= 2
            t += 1
    
        test_bases = [2, 3]
        for a in test_bases:
            if a >= x:
                continue
            y = mod_pow(a, u, x)
            if y == 1 or y == x - 1:
                continue
            for _ in range(t - 1):
                y = mod_pow(y, 2, x)
                if y == x - 1:
                    break
            else:
                return False
        return True

    for x in range(2, n + 1):
        if is_prime(x):
            number_pn += 1
    
    time_end = time.time()    
    return time_end - time_start, number_pn

# Simple trial division (for comparison)
def find_prime_simple(n):
    time_start = time.time()
    number_pn = 0
    
    def is_prime(i):
        if i < 2:
            return False
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                return False
        return True
    
    for i in range(2, n + 1):
        if is_prime(i):
            number_pn += 1
    
    time_end = time.time()    
    return time_end - time_start, number_pn

# Sieve of Eratosthenes (for comparison)
def find_prime_sieve(n):
    time_start = time.time()
    
    if n < 2:
        return 0, 0
    
    # Create a boolean array and initialize all entries as true
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    
    p = 2
    while p * p <= n:
        if prime[p]:
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    
    # Count primes
    number_pn = sum(prime)
    
    time_end = time.time()    
    return time_end - time_start, number_pn

# Test with smaller numbers first
print("Testing with n=1000:")
print("Miller-Rabin:", find_prime_miller_rabin(1000))
print("Simple method:", find_prime_simple(1000))
print("Sieve method:", find_prime_sieve(1000))

print("\nTesting with n=10000:")
print("Miller-Rabin:", find_prime_miller_rabin(10000))
print("Simple method:", find_prime_simple(10000))
print("Sieve method:", find_prime_sieve(10000))

print("\nTesting with n=100000:")
print("Miller-Rabin:", find_prime_miller_rabin(100000))
print("Sieve method:", find_prime_sieve(100000))

# Test some specific cases to verify correctness
def test_specific_primes():
    print("\nTesting specific numbers:")
    
    def is_prime_miller_rabin(x):
        if x == 2 or x == 3:
            return True
        elif x % 2 == 0 or x < 2:
            return False
    
        def mod_pow(base, exp, mod):
            result = 1
            base = base % mod
            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % mod
                base = (base * base) % mod
                exp = exp // 2
            return result
    
        u = x - 1
        t = 0
        while u % 2 == 0:
            u //= 2
            t += 1
    
        test_bases = [2, 3]
        for a in test_bases:
            if a >= x:
                continue
            y = mod_pow(a, u, x)
            if y == 1 or y == x - 1:
                continue
            for _ in range(t - 1):
                y = mod_pow(y, 2, x)
                if y == x - 1:
                    break
            else:
                return False
        return True
    
    def is_prime_simple(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    test_numbers = [2, 3, 4, 5, 17, 25, 97, 101, 121, 997, 1009]
    
    for num in test_numbers:
        miller_result = is_prime_miller_rabin(num)
        simple_result = is_prime_simple(num)
        print(f"{num}: Miller-Rabin={miller_result}, Simple={simple_result}, Match={miller_result == simple_result}")

test_specific_primes()
