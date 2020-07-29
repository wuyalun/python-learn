# #!/usr/bin/env python
# # coding=utf-8
# Group = int(input())  # 组数
# for g_val in range(Group):
#     input_str = input()
#     if input_str != "":
#         num = input_str[0]  # 每组数字个数
#         max = input_str[1]  # 默认最大值
#         exit()
#
#         break
#         input_list = input_str.split()
#
#
#
#     else:
#         break
#




T = int(input())
for t1 in range(T) :

    ns = input().split()
    n = int(ns[0])
    high = 1
    for i in range(2, n+1):
        if(ns[i]>ns[high]):
            high = i
    temp = ns[high]
    ns[high] = ns[1]
    ns[1] = temp
    low = n
    for i in range(2, n):
        if(ns[i]<ns[low]):
            low = i
    temp = ns[low]
    ns[low] = ns[n]
    ns[n] = temp
    print("Case #%d: %s" % (t1 + 1, " ".join(str(i) for i in ns[1:])))