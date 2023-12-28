class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        curr_sum = sum(nums[0:k])
        max_sum = curr_sum
        for i in range(0, len(nums) - k):
            curr_sum = curr_sum - nums[i] + nums[i+k]
            max_sum = max(max_sum, curr_sum)

        return max_sum / k

nums = [4,2,1,3,3]
print(Solution().findMaxAverage(nums, 2))
