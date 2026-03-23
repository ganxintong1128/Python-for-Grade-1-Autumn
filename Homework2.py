import time
def  find_prime(n):
    time_start = time.time()
    number_pn = 0

    def is_prime(i):
        for j in range(2,i):
            if i%j==0:
                return False
        return True
    for i in range(2,n+1):
        if is_prime(i):

            number_pn+=1

    time_end = time.time()    
    return time_end - time_start,  number_pn
print(find_prime(10))
