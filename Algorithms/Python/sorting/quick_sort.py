def quick_sort(mylist):
    if len(mylist) <= 1:
        return mylist
    pivot = mylist[len(mylist) // 2]
    less = []
    more = []
    equal = []
    for i in mylist:
        if i < pivot:
            less.append(i)
        elif i > pivot:
            more.append(i)
        else:
            equal.append(i)
    return quick_sort(less) + equal + quick_sort(more)

print(quick_sort([11, 0, 4, 5, 6 ,7, 3, 8, 2, 9, 1]))
