class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        l = 0
        r = len(nums) - 1
        amountRemovedPairs = 0
        nums.sort()
        
        if len(nums) == 1:
            return 0

        while l < r:
            if nums[l] + nums[r] > k:
                r -= 1
            elif nums[l] + nums[r] < k:
                l += 1
            else:
                amountRemovedPairs += 1
                r -= 1
                l += 1
            
        return amountRemovedPairs

nums = input().split(' ')
nums = [3,1,3,4,3]
nums = list(map(int, nums))
print(Solution().maxOperations(nums, 6)) 
