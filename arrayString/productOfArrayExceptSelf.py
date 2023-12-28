class Solution:

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        arrayResult = [1 for _ in nums]

        start = 1
        end = 1

        for i in range(len(nums)):
            arrayResult[i] = start
            start *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            arrayResult[i] *= end
            end *= nums[i]
        
        return arrayResult

print(Solution().productExceptSelf([2,3,4,5]))
