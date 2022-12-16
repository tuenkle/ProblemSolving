#TODO-0층부터 검증해서 리스트에 쌓은다음 min인덱스를 저장하면 업데이트 될 수록 고층의 최저 시간이 된다.
import sys
N, M, B = map(int, sys.stdin.readline().split())
max_height = 256
al2 = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
coordinates = []
mylist = []
while max_height >= 0:
    inventory_blocks = B
    time = 0
    for al in al2:
        for a in al:
            block = max_height - a
            if block > 0:
                inventory_blocks -= block
                time += block
            elif block < 0:
                inventory_blocks += block * (-1)
                time += block * (-2)
    if inventory_blocks >= 0:
        mylist.append((time, max_height))
    max_height -= 1
mylist.sort(key=lambda x:(x[0], -x[1]))
print(mylist[0][0], mylist[0][1])
