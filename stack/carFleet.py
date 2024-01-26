class Solution:
    def partition(self, arr, low, high, speed):
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                speed[i], speed[j] = speed[j], speed[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        speed[i+1], speed[high] = speed[high], speed[i+1]

        return i+1
    
    def quicksort(self, arr, low, high, speed):
        if low < high:
            pi = self.partition(arr, low, high, speed)
            self.quicksort(arr, low, pi - 1, speed)
            self.quicksort(arr, pi + 1, high, speed)

    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        stack = 0 
        n = len(position)
        res = n
        self.quicksort(position, 0, n-1, speed)

        for i in range(n-1, -1, -1):
            v = speed[i]
            p = position[i]

            if stack and p < stack[0]:
                pStack = stack[0]
                vStack = stack[1]
                stackTime = (target - pStack) / vStack
                time = (target - p) / v
                if time <= stackTime:
                    res -= 1
                else:
                    stack = (p, v)

            if not stack:
                stack = (p, v)

        return res

Solution().carFleet(12, [10,8,0,5,3], [2,4,1,1,3])

