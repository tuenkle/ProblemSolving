import sys
while True:
    a = sys.stdin.readline().rstrip()
    if a == ".":
        break
    mystack = []
    for char in a:
        if char == "[":
            mystack.append("]")
        elif char == "(":
            mystack.append(")")
        elif char == "]":
            if len(mystack) == 0:
                print("no")
                break
            elif mystack.pop() == "]":
                pass
            else:
                print("no")
                break
        elif char == ")":
            if len(mystack) == 0:
                print("no")
                break
            elif mystack.pop() == ")":
                pass
            else:
                print("no")
                break
    else:
        if len(mystack) != 0:
            print("no")
        else:
            print("yes")

