import math

T = int(input())
for n in range(T):
    inputStr = input()
    if inputStr != "":
        M = 0
        N = int(inputStr)
        maxN = int(math.sqrt(2*N+1/4)-1/2)
        for n1 in range(2, maxN+1):
            a1 = int((2*N-n1*(n1-1))/(2*n1))
            if a1 == 0:
                continue
            elif n1*(2*a1+n1-1)/2 == N:
                M += 1
        print("Case #%d: %d" % (n + 1 , M))
    else:
        break

import math
Group = int(input())  # 测试数据组数
for g_val in range(Group):
    inputStr = input()
    if inputStr != "":
     a = 1

    else:
        break
