import sys
n = int(sys.stdin.readline())
mystack = []
i = 1
answer_list = []
break_now = False
for _ in range(n):
    if break_now:
        break
    a = int(sys.stdin.readline())
    while True:
        if not mystack:
            mystack.append(i)
            answer_list.append("+")
            i += 1
        elif a < mystack[-1]:
            print("NO")
            break_now = True
            break
        elif a == mystack[-1]:
            mystack.pop()
            answer_list.append("-")
            break
        elif a > mystack[-1]:
            mystack.append(i)
            answer_list.append("+")
            i += 1
if not break_now:
    print("\n".join(answer_list))