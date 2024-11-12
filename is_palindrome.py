def isPalindrome(s):
	arr = []
	for i in s:
		if i.isalnum():
			arr.append(i.lower())
	return arr == arr[::-1]

s= "Was it a car or a cat I saw?"
hello = isPalindrome(s)
print(hello)

