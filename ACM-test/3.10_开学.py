T = int(input())
for t in range(T):
    N,M,D = list(map(int, input().split()))
    ns = list(map(int, input().split()))
    ds = 0
    for i in ns:
        ds += i
    ms = []
    for i in range(M):
        ms.append(list(map(int, input().split())))
    if ds<=D:
        print('Case #{}: {}'.format(t+1,'0'))
    else:
        ds = ds-D
        isOK = False
        temp = []
        for i in range(M):
            if ms[i][0]>=ds:
                isOK = True
                temp.append(ms[i][1])
        if isOK==False:
            print('Case #{}: {}'.format(t+1,'QAQ'))
        else:
            temp.sort()
            print('Case #{}: {}'.format(t+1,temp[0]))

Group = int(input())
for g_val in range(Group):
    N, M, D = map(input().split())