import sys
input = sys.stdin.readline
N, M = map(int, input().split())
mylist = []
for _ in range(M):
    u, v = map(int, input().split())
    need_append = True
    for i in mylist:
        if u in i:
            i.add(v)
            need_append = False
            break
        if v in i:
            i.add(u)
            need_append = False
            break
    if need_append:
        mylist.append({u, v})
nothing_changed = False
while not nothing_changed:
    breaker = False
    for i in range(len(mylist)):
        for j in range(i + 1, len(mylist)):
            if mylist[i].isdisjoint(mylist[j]):
                pass
            else:
                mylist[i] = mylist[i] | mylist[j]
                del mylist[j]
                breaker = True
                break
        if breaker:
            break
    else:
        nothing_changed = True
print(len(mylist))