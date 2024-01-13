class Solution:
    def removeStars(self, s: str) -> str:
        sVetor = list(s)
        starts = 0 
        i = 0

        while i < len(sVetor):
            while sVetor[-1] == '*':
                starts += 1
                sVetor.pop()
                i += 1

            while len(sVetor) and sVetor[-1] != '*' and starts > 0:
                starts -= 1
                sVetor.pop()
                i += 1
            
            if len(sVetor) and sVetor[-1] != '*':
                i += 1
                continue

        print(sVetor)
        
        return ''.join(sVetor)

print(Solution().removeStars('abcccc***c***'))

        
