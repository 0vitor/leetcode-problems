class Solution:
    def moveZeroes(self, nums: list) -> None:
        slow = 0
        for fast in range(len(nums)):
            print(array)
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # wait while we find a non-zero element to
            # swap with you
            if nums[slow] != 0:
                slow += 1

array = [1,2,3,0,4,5,0,6,7,8,0,12,0,0]

Solution().moveZeroes(array)
print(array)
