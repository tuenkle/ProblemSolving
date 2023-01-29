def selection_sort(mylist):
    for i in range(len(mylist) - 1):
        min_idx = i
        for j in range(i + 1, len(mylist)):
            if mylist[min_idx] > mylist[j]:
                min_idx = j
        mylist[i], mylist[min_idx] = mylist[min_idx], mylist[i]
    return mylist
print(selection_sort([0, 4, 5, 6 ,7, 3, 8, 2, 9, 1]))


