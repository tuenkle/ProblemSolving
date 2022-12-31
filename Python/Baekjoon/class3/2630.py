import sys

input = sys.stdin.readline
N = int(input())
al2 = [list(map(int, input().split())) for _ in range(N)]
blue = 0
white = 0


def is_same(mylist):
    global blue
    global white
    temp = mylist[0][0]
    for i in mylist:
        for j in i:
            if temp != j:
                return False
    if temp == 1:
        blue += 1
    else:
        white += 1
    return True


def myfunc(mylist):
    global white
    global blue
    a1 = []
    a2 = []
    a3 = []
    a4 = []
    for i in mylist[:len(mylist) // 2]:
        a1.append(i[:len(mylist) // 2])
    for i in mylist[:len(mylist) // 2]:
        a2.append(i[len(mylist) // 2:])
    for i in mylist[len(mylist) // 2:]:
        a3.append(i[:len(mylist) // 2])
    for i in mylist[len(mylist) // 2:]:
        a4.append(i[len(mylist) // 2:])
    if not is_same(a1):
        myfunc(a1)
    if not is_same(a2):
        myfunc(a2)
    if not is_same(a3):
        myfunc(a3)
    if not is_same(a4):
        myfunc(a4)
if is_same(al2):
    print(white)
    print(blue)
else:
    myfunc(al2)
    print(white)
    print(blue)