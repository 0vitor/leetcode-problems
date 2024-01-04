class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        n = len(nums)

        for i in range(n):
            d[nums[i]] = i

        for i in range(n):
            index = d.get(target - nums[i])
            if index and i != index:
                return [i, index]

print(Solution().twoSum([1,3,4,2], 6))
