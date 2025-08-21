# checks if a list of numbers contains any duplicates.
nums = [1,2,3,1]

def duplicate(nums: list[int]) -> bool:
    dup = set()

    for i in nums:
        if i in dup:
            print(f"number duplicated: {i}")
            return True
        print(f"not duplicated: {i}")
        dup.add(i)

    return False

print(duplicate(nums))