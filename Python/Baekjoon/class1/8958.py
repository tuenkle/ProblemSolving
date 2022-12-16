import sys
n = int(sys.stdin.readline())
mi = [sys.stdin.readline().strip() for _ in range(n)]
for i in mi:
    score = 0
    streak = 1
    for c in i:
        if c == "O":
            score += streak
            streak += 1
        else:
            streak = 1
    print(score)

