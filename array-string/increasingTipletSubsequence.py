class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        globalI = 0 
        i1 = float('inf')
        i2 = float('-inf')
        
        while globalI < len(nums) - 1:
            if i1 > nums[globalI]: i1 = nums[globalI]
            if i1 < nums[globalI]: i2 = nums[globalI]
            if i1 < i2 < nums[globalI + 1]: return True 
        
        return False

Solution().increasingTriplet([1,2,1,3])
