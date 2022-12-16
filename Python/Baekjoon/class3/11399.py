import sys
input = sys.stdin.readline
N = int(input())
al = list(map(int, input().split()))
al.sort()
answer = 0
previous_sum = 0
for i in al:
    previous_sum += i
    answer += previous_sum
print(answer)