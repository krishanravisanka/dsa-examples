nums = [-2,1,-3,4,-1,2,1,-5,4]

def sub_array(nums):
    """
    finds the contigous subarray (Kadane's Algorithms)
    Args:
      nums: a list of integers

    Return:
       Maximum sum of contigous subarray
    """
    if not nums:
        return 0
    
    curret_max = nums[0]
    global_max = nums[0]

    for i in range(1, len(nums)):
        # num = nums[i]

        curret_max = max(nums[i], curret_max + nums[i])
        global_max = max(global_max, curret_max)

    return global_max

print(sub_array(nums))