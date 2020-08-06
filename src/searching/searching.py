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

    # better yes passes! 
    # left half
    left_index = 0 
    #right half
    right_index = len(arr)-1 
    #getting to the middle 
    while right_index - left_index > 0:
        # middle index is smallest + largest // 2, not in number form index form 
        middle_index = (left_index + right_index) // 2
        # if the middle_index is larger than target
        if arr[middle_index] > target:
            # the right equals the middle_index
            right_index = middle_index
        #if  middle_index is less than target
        elif arr[middle_index] < target:
            #left equals middle_index
            left_index = middle_index
        else:
            # return the value of the middle_index
            return middle_index

    return -1 # if not found 

    # bad way, stuck in an infinity loop, not sure how to fix it right now, lost cause. 

    # current_arr = arr
    # mid_add = 0 
    ## if the current array's length is larger than 1 
    # while len(current_arr) > 1:
            ## set up mid point index
    #     mid_point = 0 
            ## if the length is greater than zero 
    #     if (len(current_arr) % 2) == 0:
                ## make the mid_point the length of the array divided by 2, for the left set side
    #         mid_point = int(len(current_arr) // 2) 
    #     else:
                ## or set up the mid_point for the left side 
    #         mid_point = int(len(current_arr) // 2 + 1)

                ## if the mid point equals the target
    #         if current_arr[mid_point] == target:
                    ## set up to return the midpoint
    #             return mid_add + mid_point
                    ## or if the target is less than midpoint
    #         elif target < current_arr[mid_point]:
                    ## mid point is set up to be the right side 
    #             current_arr = current_arr[:mid_point]
    #         else:
                    ## set up the mid point to be for the left side 
    #             mid_add = mid_point + mid_add
    #             current_arr = current_arr[mid_point:]


    # return -1  # not found
