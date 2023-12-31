class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        maxAltitude = 0
        currentAltitude = 0 
        for a in gain:
            currentAltitude += a
            if currentAltitude > maxAltitude:
                maxAltitude = currentAltitude

        return maxAltitude

gain = [-4,-3,-2,-1,4,3,2] 
print(Solution().largestAltitude(gain))
