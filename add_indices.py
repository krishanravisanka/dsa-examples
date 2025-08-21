# initializing the array
nums = [5,3,2,7]
target = 9

def add_indices(nums, target):
    numMap = {}
    for i, n in enumerate(nums):
        compliment = target - n
        if compliment in numMap:
            return [numMap[compliment], i]
        numMap[n] = i

output = add_indices(nums, target)
print(output)