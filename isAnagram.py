def isAnagram(s:str, t:str):
        hash = {}
        for i in s:
            if hash.get(i,0):
                hash[i] += 1
            else:
                hash[i] = 1
        for i in t:
            if i in hash:
                if hash[i] == 0:
                    return False
                hash[i] -= 1
            else:
                return False
        for i in hash:
            if hash[i] > 0:
                return False
        return True

answer = isAnagram("car", "raac")
print(answer)