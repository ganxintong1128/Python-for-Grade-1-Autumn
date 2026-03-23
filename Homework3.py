import time
def str2list(s: str) -> (list, int):
    if s.startswith('-'):
        sign = -1
        digits = s[1:]
    else:
        sign = 1
        digits = s.lstrip('+')  
    return [int(c) for c in reversed(digits)], sign

def list2str(lst: list, sign: int = 1) -> str:
    if not lst:
        return '0'
    while len(lst) > 1 and lst[-1] == 0:
        lst.pop()
    digits_str = ''.join(map(str, reversed(lst)))
    if sign == -1 and digits_str != '0':
        return f'-{digits_str}'
    return digits_str

def compare_list(lst1: list, lst2: list) -> int:
    if len(lst1) > len(lst2):
        return 1
    elif len(lst1) < len(lst2):
        return -1
    else:
        for a, b in reversed(list(zip(lst1, lst2))):
            if a > b:
                return 1
            elif a < b:
                return -1
        return 0

def add_list(lst1: list, lst2: list) -> list:
    result = []
    carry = 0
    max_len = max(len(lst1), len(lst2))
    for i in range(max_len):
        a = lst1[i] if i < len(lst1) else 0
        b = lst2[i] if i < len(lst2) else 0
        total = a + b + carry
        carry = total // 10
        result.append(total % 10)
    if carry > 0:
        result.append(carry)
    return result

def sub_list(lst1: list, lst2: list) -> list:
    result = []
    borrow = 0
    for i in range(len(lst1)):
        a = lst1[i] - borrow
        b = lst2[i] if i < len(lst2) else 0
        if a < b:
            a += 10
            borrow = 1
        else:
            borrow = 0
        result.append(a - b)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result

def mul_list(lst1: list, lst2: list) -> list:
    if compare_list(lst1, [0]) == 0 or compare_list(lst2, [0]) == 0:
        return [0]
    len1, len2 = len(lst1), len(lst2)
    result = [0] * (len1 + len2)  
    if len1 < len2:
        lst1, lst2 = lst2, lst1
        len1, len2 = len2, len1
    for i in range(len1):
        carry = 0
        for j in range(len2):
            total = lst1[i] * lst2[j] + carry + result[i + j]
            result[i + j] = total % 10
            carry = total // 10
        if carry > 0:
            result[i + len2] = carry
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result

def div_list(lst_dividend: list, lst_divisor: list) -> (list, list):
    if compare_list(lst_divisor, [0]) == 0:
        raise ValueError('除数不能为0')
    def strip_leading_zero(lst):
        while len(lst) > 1 and lst[-1] == 0:
            lst.pop()
        return lst
    lst_dividend = strip_leading_zero(lst_dividend.copy())
    lst_divisor = strip_leading_zero(lst_divisor.copy())
    if compare_list(lst_dividend, lst_divisor) < 0:
        return [0], lst_dividend.copy()
    quotient = []
    remainder = []
    for digit in reversed(lst_dividend):
        remainder.insert(0, digit)
        remainder = strip_leading_zero(remainder)
        q = 0
        while compare_list(remainder, lst_divisor) >= 0:
            remainder = sub_list(remainder, lst_divisor)
            q += 1
        quotient.append(q)
    quotient = strip_leading_zero(quotient[::-1])
    remainder = strip_leading_zero(remainder)
    return quotient, remainder


def pow_list(lst_base: list, n: int) -> list:
    if lst_base == 0:
        assert n != 0,f'0的底数不能为0'
        return [0]
    if n == 0:
        return [1]
    if n == 1:
        return lst_base.copy()
    result = [1]
    current_base = lst_base.copy()
    while n > 0:
        if n % 2 == 1:
            result = mul_list(result, current_base)
        current_base = mul_list(current_base, current_base)
        n = n // 2
    return result

def add(str1: str, str2: str) -> str:
    lst1, sign1 = str2list(str1)
    lst2, sign2 = str2list(str2)
    if sign1 == sign2:
        result_lst = add_list(lst1, lst2)
        return list2str(result_lst, sign1)
    else:
        cmp = compare_list(lst1, lst2)
        if cmp == 1:
            result_lst = sub_list(lst1, lst2)
            return list2str(result_lst, sign1)
        elif cmp == -1:
            result_lst = sub_list(lst2, lst1)
            return list2str(result_lst, sign2)
        else:
            return '0'

def sub(str1: str, str2: str) -> str:
    if str2.startswith('-'):
        neg_str2 = str2[1:]
    else:
        neg_str2 = f'-{str2}'
    return add(str1, neg_str2)

def mul(str1: str, str2: str) -> str:
    lst1, sign1 = str2list(str1)
    lst2, sign2 = str2list(str2)
    result_lst = mul_list(lst1, lst2)
    sign = 1 if sign1 == sign2 else -1
    return list2str(result_lst, sign)

def div(str1: str, str2: str) -> (str, str):
    if str1.startswith('-') or str2.startswith('-'):
        raise ValueError('div函数要求除数和被除数为非负整数')
    lst_dividend, _ = str2list(str1)
    lst_divisor, _ = str2list(str2)
    quotient_lst, remainder_lst = div_list(lst_dividend, lst_divisor)
    quotient_str = list2str(quotient_lst)
    remainder_str = list2str(remainder_lst)
    return quotient_str, remainder_str

def pow(str1: str, n: int) -> str:
    if n < 0:
        raise ValueError('指数n必须为非负整数')
    lst_base, _ = str2list(str1)
    result_lst = pow_list(lst_base, n)
    return list2str(result_lst)

time_start = time.time()
print(f'22222222222222+8773849905050505={add('22222222222222','8773849905050505')}')
print(f'11111111-9877344555={sub('11111111','9877344555')}')
print(f'345676778778-222222={sub('345676778778','222222')}')
print(f'123456*789={mul('123456','789')}')
print(f'8773849905050505//123={div('8773849905050505','123')[0]}')
print(f'2**66={pow('2',66)}')
print(f'2**100+3**50={add(pow('2',100),pow('3',50))}')
print(f'2*100 +123456*789-8773849905050505//123={sub(add(mul('2','100'),mul('123456','789')),div('8773849905050505','123')[0])}')
time_end = time.time()    
print(time_end - time_start)



