nums = [5, 7, 6, 3, 1, 6, 2, 4, 8]
nums2 = [5, 7, 6, 3, 1, 6, 2, 4, 8, 12, 3, 6, 11, 9, 11]

# def bubblesort(ls):
#     swapped = True
#     while swapped:
#         swapped = False
#         for i in range(len(ls) - 1):
#             if ls[i] > ls[i + 1]:
#                 ls[i], ls[i + 1] = ls[i + 1], ls[i]
#                 swapped = True


# bubblesort(nums)
# print(nums)


# def selection_sort(mass):
#     for i in range (len(mass) - 1):
#         lowest = i
#         for j in range(i + 1, len(mass)):
#             if mass[j] < mass[lowest]:
#                 lowest = j
#         mass[i], mass[lowest] = mass[lowest], mass[i]

# selection_sort(nums2)
# print(nums2)


def insertion_sort(ls):
    for i in range(1, len(ls)):
        key = ls[i]
        j = i - 1
        while ls[j] > key and j >= 0:
            ls[j + 1] = ls[j]
            j -= 1
        ls[j+1] = key
        
    return ls

insertion_sort(nums2)
print(nums2)