def bubble_sort(arr):
    for pass_number in range(len(arr)-1, 0, -1):
        for i in range(pass_number):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]