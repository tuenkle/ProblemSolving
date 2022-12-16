import sys
n = int(sys.stdin.readline())
pairs = int(sys.stdin.readline())
al2 = set([tuple(map(int, sys.stdin.readline().split())) for _ in range(pairs)])
zombie = {1}
while True:
    didSomething = False
    discarding = []
    for pair in al2:
        if pair[0] in zombie:
            zombie.add(pair[1])
            didSomething = True
            discarding.append(pair)
        elif pair[1] in zombie:
            zombie.add(pair[0])
            didSomething = True
            discarding.append(pair)
    for i in discarding:
        al2.discard(i)
    if not didSomething:
        break
print(len(zombie)-1)