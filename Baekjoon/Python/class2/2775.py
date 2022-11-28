import sys
my_dic = {}
def get_people(k, n):
    if (k, n) in my_dic:
        return my_dic[(k, n)]
    elif k == 0:
        my_dic[(k, n)] = n
        return n
    else:
        sum = 0
        for i in range(1, n + 1):
            sum += get_people(k - 1, i)
        my_dic[(k, n)] = sum
        return sum
T = int(sys.stdin.readline())
for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(get_people(k, n))

