def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    middle = int( len(lst) / 2 )
    left= merge_sort(lst[:middle])
    right= merge_sort(lst[middle:])
    result= merge(left, right)
    return result

def merge(left, right):
    result = []
    i, j = 0, 0
    left_len = len(left)
    while i < left_len and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

a=[4,3,2,4,1,5,6,7,5]
a=merge_sort(a)
print(a)
