def binary_search(arr, search_element, low, high):
    if low > high:
        return -1 
    mid = (low + high) // 2

    if arr[mid] == search_element:
        return mid 
    elif arr[mid] > search_element:
        return binary_search(arr, search_element, low, mid - 1)
    else:
        return binary_search(arr, search_element, mid + 1, high)


my_list = [1, 3, 5, 7, 9, 11, 13, 15]
search_element = int(input("enter the element you want to search:"))
result = binary_search(my_list, search_element, 0, len(my_list) - 1)

if result != -1:
    print(f"Element {search_element} found at index {result}")
else:
    print(f"Element {search_element} not found in the list.")
