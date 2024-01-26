class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        stack = []
        result = [0]*(n-1)

        for i in range(n-1, -1, -1):
            temp = temperatures.pop()

            if len(stack) and temp < stack[-1][0]:
                top = stack[-1]
                result[i] = top[1] - i        

            while len(stack) and temp >= stack[-1][0]:
                stack.pop()

            result[i] = stack[-1][1] - i
            stack.append((temp, i))
        
        return result 



print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))
