class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        startWindow = 0
        endWindow = 0
        maxNumberConsecutiveOnes = 0

        while endWindow < len(nums):
            if nums[endWindow] == 1:
                endWindow += 1
            elif k:
                k -= 1
                endWindow += 1
            elif nums[startWindow] == 1:
                startWindow += 1
            elif nums[startWindow] == 0:
                startWindow += 1
                k += 1

            currenConsecutiveOnes = endWindow - startWindow 
            if currenConsecutiveOnes > maxNumberConsecutiveOnes:
                maxNumberConsecutiveOnes = currenConsecutiveOnes

        return maxNumberConsecutiveOnes

nums = [0,0,0,1]
print(Solution().longestOnes(nums, 4))
