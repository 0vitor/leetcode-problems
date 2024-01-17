from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        maxSequence = 0
        currentSequence = 0
        used = {key: 1 for key in nums}

        for n in nums:
            if used.get(n) == 1:
                currentN = n
                while used.get(currentN + 1) == 1:
                    currentN += 1
                    used[currentN] = 0
                    currentSequence += 1
                
                r = used.get(currentN + 1)
                if r != None:
                    used[n] += r + currentSequence
                else:
                    used[n] += currentSequence
            
            maxSequence = max(maxSequence, used[n])
            currentSequence = 0 

        return maxSequence

print(Solution().longestConsecutive([1,0,-1]))
