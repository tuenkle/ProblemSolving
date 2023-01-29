def binary_search(sorted_list, target):  # iterative!! ,log2n + 1
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if target < sorted_list[mid]:
            high = mid - 1
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            return mid
    return False


print(binary_search([1, 3, 6, 8, 10], 8))
