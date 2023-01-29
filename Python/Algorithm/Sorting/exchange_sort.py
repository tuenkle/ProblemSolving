def exchange_sort(mylist):
    for i in range(len(mylist)):
        for j in range(i + 1, len(mylist)):
            if mylist[i] > mylist[j]:
                mylist[i], mylist[j] = mylist[j], mylist[i]
    return mylist

print(exchange_sort([4, 3, 6, 1, -2]))