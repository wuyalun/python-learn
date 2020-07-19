#!/usr/bin/env python
# coding=utf-8
Group = int(input())  # 组数
for g_val in range(Group):

    input_str = int(input())
    if input_str != "":

        print("Case #%d: %d" % (g_val + 1, input_str))
    else:
        break




