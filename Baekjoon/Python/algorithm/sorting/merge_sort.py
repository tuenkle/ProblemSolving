def merge_sort(mylist):
    if len(mylist) == 1:
        return mylist
    return sort_two_sorted_list(merge_sort(mylist[0:len(mylist)//2]), merge_sort(mylist[len(mylist)//2: len(mylist)]))


def sort_two_sorted_list(sorted_list1, sorted_list2):
    sorted_list = []
    while len(sorted_list1) != 0 and len(sorted_list2) != 0:
        if sorted_list1[0] < sorted_list2[0]:
            sorted_list.append(sorted_list1.pop(0))
        else:
            sorted_list.append(sorted_list2.pop(0))
    if len(sorted_list1) == 0:
        sorted_list.extend(sorted_list2)
    else:
        sorted_list.extend(sorted_list1)
    return sorted_list
print(merge_sort([11, 0, 4, 5, 6 ,7, 3, 8, 2, 9, 1]))
