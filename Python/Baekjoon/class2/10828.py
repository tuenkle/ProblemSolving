import sys
N = int(sys.stdin.readline())
mystack = []
for _ in range(N):
    cmd = sys.stdin.readline().rstrip()
    if cmd == "pop":
        if not mystack:
            print(-1)
        else:
            print(mystack.pop())
    elif cmd == "size":
        print(len(mystack))
    elif cmd == "empty":
        if not mystack:
            print(1)
        else:
            print(0)
    elif cmd == "top":
        if not mystack:
            print(-1)
        else:
            print(mystack[-1])
    else:
        mystack.append(int(cmd.split()[1]))