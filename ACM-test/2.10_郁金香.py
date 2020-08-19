#!/usr/bin/env python
# coding=utf-8
Group = int(input())
for g_val in range(Group):
    input_str = input()
    if input_str != "":
        input_list = input_str.split()
        n = int(input_list[0])  # 长
        m = int(input_list[1])  # 宽
        flowers = {}
        a = range(length)

        exit()

    else:
        break




T = int(input())
for t in range(T):
    n,m = list(map(int,input().split()))
    types = {}
    for n1 in range(n):
        rowStr = input()
        row = [rowStr[i:i+1] for i in range(0,m,1)]
        for m1 in row:
            if types.__contains__(m1):
                types[m1] += 1
            else:
                types[m1] = 1
    result = sorted(types.items(),key=lambda x:(-x[1],x[0]))
    print(len(result))
    for item in result:
        print('%d %s'%(item[1],item[0]))