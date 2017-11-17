def quick_sorting(arr, first, last):
    
    if first < last:
        pos = partition(arr, first, last)
        quick_sort(arr, first, pos-1)
        quick_sort(arr, pos+1, last)

def partition(arr, first, last):
    part = first
    for pos in range(first, last):
        if arr[pos] < arr[last]: # last is the pivot
            arr[pos], arr[part] = arr[part], arr[pos]
            part += 1
    arr[part], arr[last] = arr[last], arr[part]
    return part


numbers = [55,-88,44,-99,754,-88,5547,996,445,8885,-1,-555,6696]
print("Before Sort :",numbers)
print("\n")

quick_sorting(numbers, 0, len(numbers)-1)
print("After Sort :",numbers)
