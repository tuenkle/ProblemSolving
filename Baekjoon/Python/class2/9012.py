import sys
T = int(sys.stdin.readline())
al2 = [sys.stdin.readline().rstrip() for _ in range(T)]
for line in al2:
    current_open_parenthesis_count = 0
    for char in line:
        if char == "(":
            current_open_parenthesis_count += 1
        elif char == ")":
            if current_open_parenthesis_count == 0:
                print("NO")
                break
            else:
                current_open_parenthesis_count -= 1
    else:
        if current_open_parenthesis_count == 0:
            print("YES")
        else:
            print("NO")