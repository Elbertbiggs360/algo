def quick_sort_interface(arr):
    quick_sort(arr, 0, len(arr) - 1)


def quick_sort(unsorted_list, start_index, end_index):
    if start_index < end_index:
        partition_index = partition(unsorted_list, start_index, end_index)
        quick_sort(unsorted_list, start_index, partition_index - 1)
        quick_sort(unsorted_list, partition_index + 1, end_index)


def partition(arr, low_index, high_index):
    divider = low_index
    pivot = high_index

    for index in range(low_index, high_index):
        if arr[index] < arr[pivot]:
            arr[index], arr[divider] = arr[divider], arr[index]
            divider += 1
    arr[divider], arr[pivot] = arr[pivot], arr[divider]

    return divider