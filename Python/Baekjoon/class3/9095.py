import sys
T = int(sys.stdin.readline())
global count
global hashmap
hashmap = {}
def myfunc(number):
    if number == 0:
        global count
        count += 1
        return
    if number in hashmap:
        # global count
        count += hashmap[number]
        return
    if number >= 1:
        myfunc(number - 1)
    if number >= 2:
        myfunc(number - 2)
    if number >= 3:
        myfunc(number - 3)
for _ in range(T):
    count = 0
    n = int(sys.stdin.readline())
    myfunc(n)
    hashmap[n] = count
    print(count)
