import sys
N = int(sys.stdin.readline())
mydict = {1:0, 2:1, 3:1}
def get_min(number, previous_count):
    if number == 1:
        return
    if number % 3 == 0:
        get_min(number // 3, )