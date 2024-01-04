from collections import defaultdict

class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        row_counts = defaultdict(int)
        count = 0
        for row in grid:
            row_counts[tuple(row)] += 1

        for column in zip(*grid): 
            count += row_counts[column]
        return count

class Solution2:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        countMatches = {}
        
        for i in range(n):
            row = grid[i]
            k = str(row)
            if k not in countMatches:
                countMatches[k] = 0
            countMatches[k] += 1
        
        ans = 0
        for i in range(n):
            col = [row[i] for row in grid]

            k = str(col)
            if k in countMatches:
                ans += countMatches[k]
            
        return ans

print(Solution().equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))
print(Solution2().equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))
