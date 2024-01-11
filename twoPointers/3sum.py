from collections import defaultdict


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        d = {value: index for index, value in enumerate(nums)}

        result = set() 
        n = len(nums)
        i = 0
        j = 1
        print('dict', d)

        while i < n-1:
            while j < n:
                diff = -(nums[i] + nums[j])
                print(d.keys())
                print(nums[i], nums[j], diff)
                r = d.get(diff)
                print(r)
                if(r != None and r > j):
                    result.add(tuple(sorted([nums[i], nums[j], diff])))

                print()
                j += 1

            i += 1
            j = i+1
            print(i, '-----------')
        print('result', result)

        return list(result)

print(Solution().threeSum([-1,0,1,2,-1,-4]))

# [-4, -1, -1, 0, 1, 2]

