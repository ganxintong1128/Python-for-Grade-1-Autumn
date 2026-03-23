import time

def find_prime_miller_rabin_simple(n):
    """
    Miller-Rabin算法实现 - 不使用快速模幂运算版本
    这个版本更容易理解，但效率较低，适合学习算法原理
    """
    time_start = time.time()
    number_pn = 0
    
    def simple_pow_mod(base, exp, mod):
        """
        简单的模幂运算 - 不使用快速幂算法
        直接计算 base^exp mod mod
        注意：这种方法对于大指数会很慢，仅用于演示
        """
        if exp == 0:
            return 1
        
        result = 1
        # 直接循环exp次，每次乘以base并取模
        for i in range(exp):
            result = (result * base) % mod
            # 如果result变成0，可以提前退出
            if result == 0:
                return 0
        return result
    
    def is_prime_simple(x):
        """
        Miller-Rabin素性测试 - 简化版本
        不使用快速模幂，更容易理解算法流程
        """
        # 处理特殊情况
        if x == 2 or x == 3:
            return True
        if x < 2 or x % 2 == 0:
            return False
        
        # 第一步：将 x-1 分解为 u × 2^t 的形式
        # 其中 u 是奇数，t >= 1
        u = x - 1  # 从 x-1 开始
        t = 0      # 记录因子2的个数
        
        # 不断除以2，直到得到奇数u
        while u % 2 == 0:
            u = u // 2  # 整数除法
            t = t + 1   # 计数器加1
        
        # 现在 x-1 = u × 2^t，其中u是奇数
        
        # 第二步：选择测试基数
        # 对于小范围的数，使用[2, 3]就足够了
        test_bases = [2, 3]
        
        # 第三步：对每个基数进行Miller-Rabin测试
        for a in test_bases:
            # 如果基数大于等于待测数，跳过
            if a >= x:
                continue
            
            # 计算 a^u mod x（这里不使用快速幂）
            y = simple_pow_mod(a, u, x)
            
            # 检查必要条件1：
            # 如果 a^u ≡ 1 (mod x) 或 a^u ≡ -1 (mod x)
            # 那么这个基数通过测试，继续下一个基数
            if y == 1 or y == x - 1:
                continue  # 通过测试，检查下一个基数
            
            # 检查必要条件2：
            # 连续平方 t-1 次，看是否能得到 -1
            found_minus_one = False
            
            # 进行 t-1 次平方操作
            for i in range(t - 1):
                # y = y^2 mod x（不使用快速幂，直接计算）
                y = (y * y) % x
                
                # 如果得到 -1（即 x-1），说明通过测试
                if y == x - 1:
                    found_minus_one = True
                    break  # 找到-1，退出循环
                
                # 如果得到1但不是在第一次，说明违反了二次探测定理
                if y == 1:
                    return False  # 确定是合数
            
            # 如果经过所有平方操作都没有找到-1，说明不是素数
            if not found_minus_one:
                return False
        
        # 如果所有基数都通过了测试，认为是素数
        return True
    
    # 主循环：测试从2到n的所有数
    for i in range(2, n + 1):
        if is_prime_simple(i):
            number_pn += 1
    
    time_end = time.time()
    return time_end - time_start, number_pn

# 为了对比，这里也提供使用内置pow函数的版本
def find_prime_miller_rabin_builtin_pow(n):
    """
    Miller-Rabin算法 - 使用Python内置pow函数
    pow(base, exp, mod) 是Python内置的快速模幂函数
    """
    time_start = time.time()
    number_pn = 0
    
    def is_prime_builtin(x):
        if x == 2 or x == 3:
            return True
        if x < 2 or x % 2 == 0:
            return False
        
        # 分解 x-1 = u × 2^t
        u = x - 1
        t = 0
        while u % 2 == 0:
            u //= 2
            t += 1
        
        test_bases = [2, 3]
        for a in test_bases:
            if a >= x:
                continue
            
            # 使用Python内置的pow函数：pow(a, u, x) 计算 a^u mod x
            y = pow(a, u, x)
            
            if y == 1 or y == x - 1:
                continue
            
            for _ in range(t - 1):
                # 使用内置pow函数计算 y^2 mod x
                y = pow(y, 2, x)
                if y == x - 1:
                    break
            else:
                return False
        return True
    
    for i in range(2, n + 1):
        if is_prime_builtin(i):
            number_pn += 1
    
    time_end = time.time()
    return time_end - time_start, number_pn

# 测试代码
if __name__ == "__main__":
    print("Miller-Rabin算法对比测试")
    print("=" * 50)
    
    # 测试小数据
    test_n = 1000
    print(f"测试范围：2 到 {test_n}")
    print()
    
    # 方法1：不使用快速幂的简单版本
    print("1. 简单版本（不使用快速幂）:")
    time1, count1 = find_prime_miller_rabin_simple(test_n)
    print(f"   时间: {time1:.4f}秒, 素数个数: {count1}")
    
    # 方法2：使用Python内置pow函数
    print("2. 使用内置pow函数版本:")
    time2, count2 = find_prime_miller_rabin_builtin_pow(test_n)
    print(f"   时间: {time2:.4f}秒, 素数个数: {count2}")
    
    # 验证结果是否一致
    print(f"\n结果验证: {'一致' if count1 == count2 else '不一致'}")
    print(f"速度对比: 内置pow版本快 {time1/time2:.1f} 倍")
    
    print("\n" + "=" * 50)
    print("算法说明:")
    print("1. 简单版本容易理解，但对大数效率很低")
    print("2. 内置pow版本使用了优化的快速幂算法")
    print("3. 实际应用中应该使用快速幂算法")
    print("4. 这里的简单版本仅用于学习算法原理")
