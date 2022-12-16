import sys
M, N = map(int, sys.stdin.readline().split())

def get_prime_list_under_number(max):
    prime_list = [2]
    if max == 1 or max == 2:
        return prime_list
    for i in range(3, max + 1):
        is_prime = True
        for j in prime_list:
            if j > i ** 0.5:
                break
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(i)
    return prime_list

for i in get_prime_list_under_number(N):
    if i >= M:
        print(i)
