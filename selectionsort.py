def selection_sort(unsorted_list):
    for slot_to_fill in range(len(unsorted_list) - 1, 0, -1):
        biggest_num_pos = 0
        for pos in range(1, slot_to_fill + 1):
            if unsorted_list[pos] > unsorted_list[biggest_num_pos]:
                biggest_num_pos = pos
        unsorted_list[slot_to_fill], unsorted_list[biggest_num_pos] = unsorted_list[biggest_num_pos], unsorted_list[slot_to_fill]