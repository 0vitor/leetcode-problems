class Solution:
    def compress(self, chars: list[str]) -> int:
        counter = 1
        n = len(chars)

        if n == 1:
            return n

        i = 0
        while i < len(chars) - 1:
            if chars[i] == chars[i+1]:  
                counter += 1
                del chars[i+1]
            else: 
                if counter > 1:
                    for c in range(len(str(counter))):
                        chars.insert(i+1, str(counter)[c])
                        i+=1
                counter = 1
                i += 1
        
        if counter > 1:
            for c in str(counter):
                chars.append(c)

        return len(''.join(chars))
 
chars = ["r","r","u","n","n","n","n","n","n","n","n","n","n","n","u", "u"]
print(Solution().compress(chars))
print(chars)
