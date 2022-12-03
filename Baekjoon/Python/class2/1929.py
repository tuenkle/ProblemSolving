import sys

M, N = map(int, sys.stdin.readline().split())

prime_list = [2]

def set_prime_list_under_number(max):
    for n in range(3, max):
        for i in prime_list:
            if n % i == 0:
                pass
        prime_list.append(n)
        return True
def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in prime_list:
            if n % i == 0:
                return False
        if n < 1000:
            prime_list.append(n)
        return True
for i in range(M , N + 1):
    if is_prime(i):
        print(i)
