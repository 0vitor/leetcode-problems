class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1
        currentLeftSum = 0
        currentRightSum = 0

        while l < r:
            print("left: ", currentLeftSum)
            print("right: ", currentRightSum)
            print()
            if currentLeftSum + nums[l] > currentRightSum + nums[r]:
                currentRightSum += nums[r]
                r -= 1
            elif currentLeftSum + nums[l] < currentRightSum + nums[r]:
                currentLeftSum += nums[l]
                l += 1
            else:
                l += 1
                r -= 1


        print("left: ", currentLeftSum)
        print("right: ", currentRightSum)
        print()

        if currentRightSum == currentLeftSum and l == r:
            return l
        return -1

gain = [-1,-1,-1,-1,0,1] 
print(Solution().pivotIndex(gain))
