import sys
a = sys.stdin.readline().strip()
myDic = {}
for i in a:
    upper_i = i.upper()
    myDic[upper_i] = myDic.get(upper_i, 0) + 1
max_value = 0
max_key = ""
two_max = False
for i in myDic:
    upper_i = i.upper()
    if myDic[upper_i] == max_value:
        two_max = True
    elif myDic[upper_i] > max_value:
        max_value = myDic[upper_i]
        two_max = False
        max_key = upper_i
if (two_max):
    print("?")
else:
    print(max_key)