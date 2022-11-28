import sys
prime_set = {2}
not_prime_set = {1}
def is_prime(x):
    if x in prime_set:
        return True
    elif x in not_prime_set:
        return False
    else:
        for i in range(2, x):
            if x % i == 0:
                not_prime_set.add(x)
                return False
    prime_set.add(x)
    return True
N = int(sys.stdin.readline())
il = map(int, sys.stdin.readline().split())
count = 0
for i in il:
    if is_prime(i):
        count += 1
print(count)