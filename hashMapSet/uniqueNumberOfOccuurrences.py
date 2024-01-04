class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        countRepetitions = {}
        setRepetiotions = set()
        for n in range(len(arr)):
            if not countRepetitions.get(arr[n]):
                countRepetitions[arr[n]] = 1
            else:
                countRepetitions[arr[n]] += 1
        
        for repetitions in countRepetitions.values():
            if repetitions in setRepetiotions:
                return False
            else:
                setRepetiotions.add(repetitions)

        return True


print(Solution().uniqueOccurrences([1,2,2,1,1,3]))
