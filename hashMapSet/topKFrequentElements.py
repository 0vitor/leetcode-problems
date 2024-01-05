from collections import Counter

class Solution:
    
    def partition(self, arr, low, high):
        pivot = arr[low][1]
        i = low
        # print('pivo = ', pivot)

        for j in range(low+1, high):
            if arr[j][1] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i], arr[low] = arr[low], arr[i]
        return i

    def quick_select(self, arr, low, high, k):
        if low <= high:
            pivot_index = self.partition(arr, low, high)
            # print(pivot_index)
            # print()

            if pivot_index == k:
                return arr[pivot_index]
            elif pivot_index < k:
                return self.quick_select(arr, pivot_index + 1, high, k)
            else:
                return self.quick_select(arr, low, pivot_index - 1, k)

    def topKFrequent(self, nums: list[int], k: int):
        c = Counter(nums)
        response = list(c.items())
        self.quick_select(response, 0, len(response), len(response)-k-1)
        l = []
        for i in response[len(response)-k:]:
            l.append(i[0])
        return l 
        

# Exemplo de uso:
arr = [3, 1, 4, 4, 2, 2, 5, 3]
# k = 3  # Encontrar o terceiro menor elemento

# result = quick_select(arr, 0, len(arr) - 1, k - 1)

print(Solution().topKFrequent([1,1,1,2,2,3], 2))
