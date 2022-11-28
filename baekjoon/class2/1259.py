import sys
while True:
    a = sys.stdin.readline().rstrip()
    if a == "0":
        break
    is_palindrome = True
    for i in range(len(a) // 2):
        if a[i] != a[-i-1]:
            is_palindrome = False
            break
    if is_palindrome:
        print("yes")
    else:
        print("no")


