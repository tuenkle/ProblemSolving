import sys
input = sys.stdin.readline
T = int(input())
fibonacci_print01_list = [(1, 0), (0, 1)]
def fibonacci(n):
    if n < len(fibonacci_print01_list):
        return fibonacci_print01_list[n]
    else:
        fibonacci_print01_list.append((fibonacci(n-1)[0] + fibonacci(n-2)[0], fibonacci(n-1)[1] + fibonacci(n-2)[1]))
        return fibonacci_print01_list[n]
for _ in range(T):
    print(" ".join(str(i) for i in fibonacci(int(input()))))
