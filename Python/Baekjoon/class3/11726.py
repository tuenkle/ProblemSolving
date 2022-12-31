import sys
n = int(sys.stdin.readline())
hashmap = {1:1, 2:2}
def myfunc(count, number):
    if number in hashmap:
        return hashmap[number]
    else:
        hashmap[number] = myfunc(count, number - 1) + myfunc(count, number - 2)
        return hashmap[number]
print(myfunc(0, n) % 10007)
