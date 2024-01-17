class Solution:
    def calculateRightSide(self, height) -> int:
        amountRain = 0
        n = len(height)
        i = n-1
        j = i - 1 
        while i > 0:
            while height[j] < height[i] and j > 0:
                j -= 1

            distance = (i - j - 1)
            totalArea = height[i] * distance

            for k in height[j + 1:i]:
               totalArea -= k 
            amountRain += totalArea
            
            i = j
            j = i - 1
        
        return amountRain 


    def trap(self, height: list[int]) -> int:
        i = 0
        j = 1
        n = len(height)
        amountRain = 0

        while i < n - 1:
            while j < n and height[j] < height[i]:
                j += 1

            if j == n:
                return amountRain + self.calculateRightSide(height[i:j+1])

            distance = j - i - 1
            totalArea = height[i] * distance
            for k in height[i+1:j]:
                totalArea -= k
                
            amountRain += totalArea
            i = j
            j += 1 

        return amountRain

print(Solution().trap([0,1,0,2,1,0,1,3,2,0,0,2,4,0,1,2]))
