def linear_search(arr, target):
    # Your code here
    for num in range(len(arr)):
        if arr[num] == target:
            return num 
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here

    # understand plan 
    # divide in half
    # if equals, return true
    # if smaller, return left half
    # else return right target
    # if at the end, return false 

    # better?
    left_index = 0 
    right_index = len(arr)-1
    while right_index - left_index > 0:
        middle_index = (left_index + right_index) // 2
        if arr[middle_index] > target:
            right_index = middle_index
        elif arr[middle_index] < target:
            left_index = middle_index
        else:
            return middle_index

    return -1 # not found 

    # bad way 
    # current_arr = arr
    # mid_add = 0 
    # while len(current_arr) > 1:
    #     mid_point = 0 
    #     if (len(current_arr) % 2) == 0:
    #         mid_point = int(len(current_arr) // 2) 
    #     else:
    #         mid_point = int(len(current_arr) // 2 + 1)

    #         if current_arr[mid_point] == target:
    #             return mid_add + mid_point
    #         elif target < current_arr[mid_point]:
    #             current_arr = current_arr[:mid_point]
    #         else:
    #             mid_add = mid_point + mid_add
    #             current_arr = current_arr[mid_point:]

    # if len(current_arr) == 1:
    #     if current_arr[0] == target:
    #         return 0 

    # return -1  # not found
