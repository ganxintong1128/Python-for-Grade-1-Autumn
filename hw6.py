#1
def f(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return f(f(n//2))+1
#2
def f1(n):
    if n == 0 or n == 1:
        return 1
    else:
        return f1(n-1)+f1(n-2)
def f2(n):
    if n==0 or n==1 or n==2:
        return 1
    else:
        return f2(n-1)+2*f2(n-2)-f2(n-3)
def f3(n):
    if n==0:
        return 2
    if n==1:
        return 3
    return f3(n-1)*f3(n-2)
def f4(m,n):
    if m == 0 or n == 0:
        return 1
    return f4(m,n-1)+f4(m-1,n)-f4(m-1,n-1)
#3
def list_sum(lst):
    total=0
    for i in lst:
        if isinstance(i,list):
            total+=list_sum(i)
        else:
            total+=i
    return total
#4
def time_count(lst):
    count_dict={}
    for i in lst:
        if isinstance(i,list):
            time_count(i)
        else:
            count_dict[i]=count_dict.get(i,0)+1
    return count_dict
lst=[1, 2, 3, 4, 5, 6, [3,4,5,6], [5,6]]
print(time_count(lst))