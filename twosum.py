def twoSum(nums, target):
    #make a hashmap of every value
    map = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in map:
            return [diff, n]
        map[n] = i

print(twoSum([1,2,3,1],4))