class Solution:
    def gen(self, n, lenStack):
        if lenStack == 0:
            return [{'p': '(', 'lp': 1, 'rp': 0}]
        else:
            r = self.gen(n, lenStack-1)
            lenR = len(r)
            for i in range(lenR):
                left = r[i].get('lp')
                right = r[i].get('rp')
                lastChar = r[i].get('p')[-1]

                if left < n: 
                    if lastChar == "(":
                        r.append({'p': r[i].get('p') + ')', 'rp': right+1, 'lp': left})

                        r[i]['p'] += '('
                        r[i]['lp'] += 1

                    if lastChar == ")":
                        if left > right:
                            r.append({'p': r[i].get('p') + ')', 'rp': right+1, 'lp': left})

                        r[i]['p'] += '('
                        r[i]['lp'] += 1
                else:
                    r[i]['p'] += ')'
                    r[i]['rp'] += 1 

            return r

    def generateParenthesis(self, n: int) -> list[str]:
        return [elem['p'] for elem in self.gen(n, n*2-1)] 

print(Solution().generateParenthesis(4))

class Solution2:
    def generateParenthesis(self, n: int) -> list[str]:
        def dfs(left, right, s):
            if len(s) == n * 2:
                res.append(s)
                return 

            if left < n:
                dfs(left + 1, right, s + '(')

            if right < left:
                dfs(left, right + 1, s + ')')

        res = []
        dfs(0, 0, '')
        return res
