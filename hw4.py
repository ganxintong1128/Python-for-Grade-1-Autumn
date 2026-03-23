#1
def list_calculate(lst):
    '''给定一个list的数,求其 和 和 乘积'''
    total=0
    product=1
    for i in lst:
        total+=int(i)
        product*=int(i)
    return total,product
#2
def compare_list(lst1, lst2):
    def is_contained(a,b):
        for i in a:
            if a.count(i)>b.count(i):
                return False
            return True
    if is_contained(lst1,lst2):
        print(lst2)
        return True
    elif is_contained(lst2,lst1):
        print(lst1)
        return True
    else:
        return False
#3
valid_numbers = []
even_digits = ['0', '2', '4', '6', '8']
for num in range(1000,3001):
    num_str = str(num)
    is_valid = True
    for digit in num_str:
        if digit not in even_digits:
            is_valid = False
            break
    if is_valid:
        valid_numbers.append(num_str)
for n in valid_numbers:
    print(f'{n}', end=' ')
print()
#4
lst=[12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
result=[]
seen_num=[]
for i in lst:
    if i not in seen_num:
        result.append(i)
        seen_num.append(i)
print(result)
#5
def reverse_integer(num):
    is_positive = True
    if num < 0:
        is_positive = False
        num_str = str(num)[1:]
    elif num == 0:
        return 0
    else:
        num_str = str(num)
    digit_list = list(num_str)
    digit_list.reverse()      
    reversed_num = 0
    for digit_char in digit_list:
        reversed_num = reversed_num * 10 + int(digit_char)
    if is_positive:
        return reversed_num
    else:
        return -reversed_num
#6
def get_list_intersection(input1, input2):
    def turn_to_num_list(data):
        num_list = []
        str_list = data.split(',')
        for s in str_list:
            num = int(s)
            num_list.append(num)
        return num_list
    list1 = turn_to_num_list(input1)
    list2 = turn_to_num_list(input2)
    intersection = []
    for item in list1:
        is_in_list2 = False
        for x in list2:
            if x == item:
                is_in_list2 = True
                break  
        is_in_inter = False
        for y in intersection:
            if y == item:
                is_in_inter = True
                break
        if is_in_list2 and not is_in_inter:
            intersection.append(item)
    if len(intersection) > 0: 
        return intersection
    else:
        print("no intersection")
        return False
#7
def print_star(n):
    for i in range(1,n+1):
        print('*'*i)
    for i in range(n-1,0,-1):
        print('*'*i)     #不知道怎么写成nested for loop
#8
def count_digits(n):
    num = str(n)
    lst = list(num)
    digit_count = [0] * 10
    for digit in range(10):
        digit_str = str(digit)
        digit_count[digit] = lst.count(digit_str)
    print(f"数字 {n} 的各数字出现次数：")
    for digit in range(10):
        count = digit_count[digit]
        if count > 0:
            print(f"{digit}: {count}")
#9
def sum_of_two(n):
    total=0
    for i in range(1,n+1):
        num_two=int(str(2)*i)
        total+=num_two
    return total
#10
matrix_A = []
for row_count in range(10):  
    current_row_A = list(range(1, 11)) 
    matrix_A.append(current_row_A)
matrix_B = []
for row_num in range(1, 11): 
    current_row_B = [row_num] * 10  
    matrix_B.append(current_row_B)
print("矩阵 A:")
for row in matrix_A:
    print(row)
print("矩阵 B:")
for row in matrix_B:
    print(row)
#11
def find_min(lst):
    n = len(lst)
    is_incr = [False] * n
    is_incr[0] = True  
    for i in range(1, n):
        is_incr[i] = is_incr[i-1] and (lst[i-1] <= lst[i])
    is_decr = [False] * n
    is_decr[-1] = True 
    for i in range(n-2, -1, -1):
        is_decr[i] = is_decr[i+1] and (lst[i] >= lst[i+1])
    for i in range(n):
        if is_incr[i] and is_decr[i]:
            return i
#12
def is_prime(n):
    x=int(n**0.5)
    for i in range(2,x+1):
        if n%i==0:
            return False
        break
    return True
def eratosthenes(n):
    prime = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False
    primes_result = []  
    for x in range(2, n + 1):  
        if prime[x]: 
            primes_result.append(x)  
    return primes_result  

if __name__=='__main__':
    n=int(input('请输入一个数n以判断它是否为素数:'))
    if is_prime(n):
        print(f'{n}是素数')
    else:
        print(f'{n}不是素数')
    print(eratosthenes(1000000))