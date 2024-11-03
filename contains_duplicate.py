def hasDuplicate(nums):
	#iterate through each item and add it to hash table or if it's in there return true
	hash = set()
	for i in nums:
		if i in hash:
			return True
		else:
			hash.add(i)
	return False

answer = hasDuplicate([1,3,3])
print(answer)