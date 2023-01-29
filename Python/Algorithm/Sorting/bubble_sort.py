def bubble_sort(mylist):
    for i in range(len(mylist) - 1):
        for j in range(len(mylist) - 1 - i):
            if mylist[j] > mylist[j + 1]:
                mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]
    return mylist
print(bubble_sort([0, 4, 5, 6 ,7, 3, 8, 2, 9, 1]))

