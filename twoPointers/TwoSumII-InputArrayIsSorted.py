class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            while l < r and numbers[l] + numbers[r] > target:
                r -= 1

            while l < r and numbers[l] + numbers[r] < target:
                l += 1
        
            if numbers[l] + numbers[r] == target:
                return [l, r]

class Solution2:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        d ={value: index for index, value in enumerate(numbers)} 
        i = 0
        j = 0
        print(d)
        for n in range(len(numbers)):
            i = n
            j = d.get(target - numbers[n])
            if j:
                return [i+1, j+1]

# print(Solution().twoSum([2,7,11,15], 9))
# print(Solution().twoSum([-1, 0], -1))
# print(Solution().twoSum([2,3,4], 6))

print(Solution2().twoSum([2,7,11,15], 9))
print(Solution2().twoSum([-1, 0], -1))
print(Solution2().twoSum([2,3,4], 6))
