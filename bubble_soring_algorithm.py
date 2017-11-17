def bubble(arr):

    def swap_number(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped_number = True
    while swapped_number:
        swapped_number = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                swap_number(i - 1, i)
                swapped_number = True

numbers = [55,-88,44,-99,754,-88,5547,996,445,8885,-1,-555,6696]
print("Before Sort :",numbers)
print("\n")

bubble(numbers)
print("After Sort Bubble Sort:",numbers)
