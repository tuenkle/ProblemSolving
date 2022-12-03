import sys
K = int(sys.stdin.readline())
mystack = []
for _ in range(K):
    a = int(sys.stdin.readline())
    if a == 0:
        mystack.pop()
    else:
        mystack.append(a)
print(sum(mystack))
