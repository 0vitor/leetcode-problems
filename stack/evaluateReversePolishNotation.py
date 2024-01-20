import math
class Solution:
    def isnumber(self, value):
        try:
             float(value)
        except ValueError:
             return False
        return True

    def evalRPN(self, tokens: list[str]) -> int:
        operations = {'+', '-', '/', '*'}
        result = []
        signals = []
        r = 0
        while len(tokens):
            token = tokens.pop() 
            if self.isnumber(token):

                if len(result) and result[-1] in operations:
                    result.append(token)
                    r = int(eval(result.pop() + result.pop() + result.pop()))
                    result.pop()
                    while len(result) and result[-1] in operations:
                        r = int(eval(str(r) + result.pop() + result.pop()))
                        result.pop()
                    result.append(str(r))
                    if len(signals):
                        result.append(signals.pop())

                elif len(signals):
                    result.append(token)
                    result.append(signals.pop())
            else:
                result.append('(')
                signals.append(token)


        return int(result[0])

tokens =["4","13","5","/","+"] 
print(Solution().evalRPN(tokens))
