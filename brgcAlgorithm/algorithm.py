def brgc(n):
    if n == 1:
        return ['0','1']
    else:
        l1 = brgc(n-1)
        l2 = list(reversed(l1))

        for i in range(len(l1)):
            l1[i] = l1[i] + '0'
            l2[i] = l2[i] + '1'
        l1 += l2
        return l1

print(brgc(3))
