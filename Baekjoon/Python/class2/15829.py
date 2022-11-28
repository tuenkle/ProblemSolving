import sys
L = int(sys.stdin.readline())
a = sys.stdin.readline().rstrip()
ans = 0
square = 0
for i in a:
    int_i = ord(i) - 96
    ans += int_i * (31 ** square)
    square += 1
print(ans % 1234567891)
