import sys
N = int(sys.stdin.readline())
al = list(map(int, sys.stdin.readline().split()))
mydict = {}
for i in al:
    mydict[i] = mydict.get(i, 0) + 1
M = int(sys.stdin.readline())
a2l = map(int, sys.stdin.readline().split())
for i in a2l:
    print(mydict.get(i, 0), end=" ")
