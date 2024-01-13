class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        asteroids.reverse()
        ans = [asteroids.pop()]

        while len(asteroids):
            n = asteroids[-1]

            if not len(ans):
                ans.append(asteroids.pop())
            elif ans[-1] > 0 and n < 0:
                if ans[-1] < abs(n):
                    ans.pop()
                elif ans[-1] == abs(n):
                    ans.pop()
                    asteroids.pop()
                else:
                    asteroids.pop()
            else:
                ans.append(asteroids.pop())
                

        return ans

class Solution2:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        s = []
        for num in asteroids:
            while s and s[-1]>0 and num<0:
                if s[-1]+num<0 : s.pop()
                elif s[-1]+num>0 : break
                else: s.pop(); break
            else: s.append(num)
        return s

print(Solution().asteroidCollision([30,-10,-35,30,4,-10,50,-100]))

            
                
