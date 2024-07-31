def combine_elements(list1, list2):
    # Merge the two lists
    combined_list = list1 + list2

    # Sort the combined list by the left position
    combined_list.sort(key=lambda x: x['positions'][0])

    # Initialize the result list
    result = []

    # Iterate through the sorted list and combine elements if necessary
    i = 0
    while i < len(combined_list):
        current = combined_list[i]
        j = i + 1
        while j < len(combined_list):
            next_element = combined_list[j]
            current_left, current_right = current['positions']
            next_left, next_right = next_element['positions']

            # Check if more than half of the next element is contained within the current element
            if next_left >= current_left and next_right <= current_right and (next_right - next_left) > (
                    current_right - current_left) / 2:
                # Combine values and adjust positions
                current['values'].extend(next_element['values'])
                # Update the right position if necessary
                current['positions'][1] = max(current_right, next_right)
                # Remove the next element as it is now combined
                combined_list.pop(j)
            else:
                j += 1
        result.append(current)
        i += 1

    return result


# Example usage
list1 = [
    {"positions": [1, 4], "values": [10, 20]},
    {"positions": [5, 8], "values": [30, 40]}
]

list2 = [
    {"positions": [2, 3], "values": [50]},
    {"positions": [6, 7], "values": [60]}
]

combined_list = combine_elements(list1, list2)
print(combined_list)
