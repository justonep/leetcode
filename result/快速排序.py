def quick_sort(array, left, right):
    if left >= right:
        return
    base = left
    key = array[base]
    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
    array[right] = key
    # quick_sort(array, low, left - 1)
    # quick_sort(array, left + 1, high)

sort=[6,1 , 2, 7 , 9  ]
quick_sort(sort,0,len(sort)-1)
print(sort)