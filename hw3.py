import math
#1
def is_triangle(a, b, c):
    """
    判断所给数能否构成三角形
    直接返回True和False
    """
    # 验证三边能否构成三角形（正数 + 最长边 < 另外两边之和）
    sides = [a, b, c]
    max_side = max(sides)
    sum_others = sum(sides) - max_side  # 另外两边之和
    if max_side<sum_others:
        return True
    else:
        return False
    
if __name__=="__main__":
    try:
        a=int(input("请输入第一个数："))
        b=int(input("请输入第二个数："))
        c=int(input("请输入第三个数："))
    except ValueError:
        print("输入错误")
    else:
        if is_triangle(a,b,c):
            print('能构成三角形')
        else:
            print('不能构成三角形')

#2
def delta(a, b, c):
    '''
    判断a*x**2+b*x+c=0有几个实根,返回实根的数量和相应的根。
    '''
    if a==0:
        x=-c/b
        return 1,x
    else:
        calc=b**2-4*a*c
        if calc>=0:
            x1=(-b+calc**0.5)/(2*a)
            x2=(-b-calc**0.5)/(2*a)
            if x1==x2:
                return 2,x1
            else:
                return 2,x1,x2
if __name__=='__main__':
    try:
        a=int(input("请输入第一个数："))
        b=int(input("请输入第二个数："))
        c=int(input("请输入第三个数："))
    except ValueError:
        print('输入错误')
    else:
        print(delta(a,b,c))

#3
def is_prime(n):
    '''
    判断n是否为质数,返回True和False
    '''
    i=2
    if n<=1:
        return False
    else:
        while i<=n**0.5:
            x=n%i
            if x==0:
                return False
            else:
                i+=1
        return True
if __name__=='__main__':
    try:
        n=int(input('请输入一个正整数n:'))
    except ValueError:
        print('输入错误')
    else:
        if is_prime(n):
            print('n是质数')
        else:
            print('n不是质数')

#4
def is_palindrome_year(year):
    '''
    判断一个年份是不是回文年，譬如 2002, 1991, 1221都是回文
    '''
    a=year//1000
    b=(year%1000)//100
    c=(year%100)//10
    d=year%10
    if a==d:
        if b==c:
            return True
        else:
            return False
    else:
        return False
if __name__=='__main__':
    try:
        year=int(input('请输入4位数年份：'))
    except ValueError:
        print('输入错误！')
    else:
        if is_palindrome_year(year):
            print('是回文年')
        else:
            print('不是回文年')

#5
def f(x):
    if x<-2:
        return x**4
    elif -2<=x<2:
        return math.sin(x)
    else:
        return math.exp(x)
if __name__=='__main__':
    x=float(input('请输入一个数x：'))
    y=f(x)
    print(y)

#6
def inverse_number(num):
    '''
    返回一个数的逆序表示，例如19-->91, 102-->201, 123-->321
    '''
    return int(str(num)[::-1])

if __name__=='__main__':
    while True:
        try:
            x = int(input("请输入一个数字："))
            if x == 0:
                print("程序终止")
                break
            elif x == -1:
                continue
            else:
                inverse = inverse_number(x)
                print(f'{x} 的逆序表示为: {inverse}')
        except ValueError:
            print("输入错误，请输入一个整数")

#7
x=int(input('请输入一个整数：'))
n=x
i=0
while True:
    y=x%10
    if y==0:
        x=x//10
        i+=1
        continue
    else:
        print(f'{n}的末尾有{i}个0')
        break

#8
def Hamming(a, b):
    '''
    计算两个数的Hamming距离
    定义：两个数的二进制表示中，对应位不同的位数
    '''
    xor_result = a ^ b  
    return bin(xor_result).count('1')


if __name__ == '__main__':
    try:
        a = int(input('请输入第一个数：'))
        b = int(input('请输入第二个数：'))
    except ValueError:
        print('输入错误！请输入合法整数。')
    else:
        d = Hamming(a, b)
        print(f'{a}和{b}的Hamming距离为{d}')

#9
def is_valid(n):
    '''
    判断给定整数n是否满足3n+1猜想（最终收敛到1）
    '''
    current = n  
    while current != 1:
        if current % 2 == 0:
            current = current // 2
        else:
            current = 3 * current + 1
        if current <= 0:
            return False
    return True
if __name__ == "__main__":
    MAX_NUM = 10 ** 6
    first_invalid = None
    print(f"=== 开始验证1到{MAX_NUM}的3n+1猜想 ===")
    for num in range(1, MAX_NUM + 1):
        if num % 100000 == 0:
            print(f"已验证到 {num}")
        if not is_valid(num):
            first_invalid = num
            break
    print("\n=== 验证结束 ===")
    if first_invalid is not None:
        print(f"发现不满足的数：{first_invalid}")
    else:
        print(f"1到{MAX_NUM}范围内所有数都满足3n+1猜想！")

#10
remainder_3 = 2    
remainder_5 = 3    
remainder_7 = 2    
coeff_3 = 70       
coeff_5 = 21       
coeff_7 = 15       
lcm_357 = 105      

base_solution = remainder_3 * coeff_3 + remainder_5 * coeff_5 + remainder_7 * coeff_7
print(f"步骤1：计算基础解 = 2×70 + 3×21 + 2×15 = {base_solution}")
min_solution = base_solution
while min_solution >= lcm_357:  
    min_solution -= lcm_357
print(f"步骤2：最小正解 = {base_solution} - 105k = {min_solution}")
solutions = []
current = min_solution  
max_limit = 100000      
while current <= max_limit:
    solutions.append(current)
    current += lcm_357  
print(f"\n=== 0到{max_limit}内的解汇总 ===")
print(f"最小解：{min_solution}")
print(f"解的总个数：{len(solutions)} 个")
print(f"前10个解：{solutions[:10]}（省略中间解）")
print(f"最后1个解：{solutions[-1]}")  

#11
def fractal(n):
    """
    (a) 计算n的阶乘（n!），处理非负整数
    规则：0! = 1，1! = 1，n! = n × (n-1) × ... × 2 × 1（n≥2）
    """
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def choose(n, k):
    """
    (b) 计算组合数C(n,k) = n!/(k!·(n-k)!)，即n个元素选k个的方式数
    规则：k<0或k>n时，C(n,k)=0（无法选择）；否则按公式计算
    """
    if k < 0 or k > n:
        return 0
    numerator = fractal(n)          
    denominator = fractal(k) * fractal(n - k)  
    return numerator // denominator

if __name__ == "__main__":   
    try:
        n=int(input('请输入阶数：'))
    except ValueError:
        print('输入错误！')
    else:
        if n <= 0:
            print("错误：杨辉三角大小n必须是正整数（如n=5表示5行）")
        print(f"=== 大小为{n}的杨辉三角 ===")
        for i in range(n):
            print(" " * (n - i - 1), end="")
            for k in range(i + 1):
                print(choose(i, k), end=" ")
            print()