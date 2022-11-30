def insertion_sort(mylist):
    for i in range(1, len(mylist)):
        for j in range(i, 0, -1):
            if mylist[j - 1] > mylist[j]:
                mylist[j - 1], mylist[j] = mylist[j], mylist[j - 1]
    return mylist
print(insertion_sort([11, 0, 4, 5, 6 ,7, 3, 8, 2, 9, 1]))
