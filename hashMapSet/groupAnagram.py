from collections import Counter

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = {}
        i = 0
        result = []
        for word in strs:
            tuple_key = tuple(sorted(Counter(word).items()))

            if tuple_key not in d:
                d[tuple_key] = i
                result.append([word])
                i += 1
            else:
                result[d[tuple_key]].append(word)
            
        print(d) 
        print(result)
        return result

input = ["eat","tea","tan","ate","nat","bat"]
input = ['f']
Solution().groupAnagrams(input)
