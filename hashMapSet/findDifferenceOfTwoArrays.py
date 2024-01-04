class Solution:
    def findDifferenceForOne(self, nums1: list[int], nums2: list[int]) -> list[int]:
        i = 0
        j = 0
        result = set()
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                i += 1
            elif nums1[i] < nums2[j]:
                result.add(nums1[i])
                i += 1

            elif nums1[i] > nums2[j]:
                j += 1

        while i < len(nums1):
            result.add(nums1[i])
            i += 1
        
        return list(result)

    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        (nums1).sort()
        (nums2).sort()
        newArray1 = self.findDifferenceForOne(nums1, nums2)
        newArray2 = self.findDifferenceForOne(nums2, nums1)

        return [newArray1, newArray2]

print(Solution().findDifference([1,2,3,3], [1,1,2,2]))           

nums1 = [2,4,6]
nums2 = [1,1,2,3]
i = 0
j = 0
