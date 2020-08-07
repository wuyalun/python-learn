"""
1/3 = 0.3333333333333333 目前支持16位 > 9位
0.12341234123412341
"""
# print(1234/9999)
#
# Group = int(input())
# for g_val in range(Group):
#     a, b = list(map(int, input().split()))
#     container = []
#     result = str(int(a / b)) + '.'
#     isFind = False
#     for i in range(9):
#         temp = a * 10 % b
#         if temp == 0:
#             break
#         else:
#             if temp in container:
#                 isFind = True
#                 break
#             else:
#                 result += str(int(a * 10 / b))
#                 print(result)
#                 a = temp
#                 container.append(temp)
#     if isFind:
#         print('Case #{}: {}'.format(g_val + 1, result))
#     else:
#         print('Case #{}: {}'.format(g_val + 1, 'heiheihei'))


string = str(1234/9999)
max_i = 9  # 默认最大循环节为9

pos = string.index(".")

left = str(string)[pos+1:max_i]
right = str(string)[max_i:]



print(left)
print(right)

