class Solution:
    def calculateMaxArea(self, h, i, j):
        area = 0
        if h[i] > h[j]:
            area = h[j] * (i - j)
        else:
            area = h[i] * (i - j) 
        return abs(area)


    def maxArea(self, height: list[int]) -> int:
        length = len(height)
        i = 0
        j = length - 1

        currentMaxArea = self.calculateMaxArea(height, i, j)

        while i < j:

            if height[i] < height[j] and i + 1 <= j:
                i += 1
            elif j - 1 >= i:
                j -= 1
            
            area = self.calculateMaxArea(height, i, j)
            if area > currentMaxArea:
                currentMaxArea = area 

        return currentMaxArea

height = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(height))
