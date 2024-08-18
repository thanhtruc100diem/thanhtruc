# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:33:59 2024

@author: Student
"""

x = float(input("Nhập độ dài đoạn đường đến trường (m):"))
if x < 300:
    print("Đường đến trường quá gần. Thôi! Đi bộ")
elif x > 1200:
    print("Đường đến trường quá xa. Thôi! Đi xe máy")
elif x >= 300 and x <= 700:
    print("Đường đến trường không xa. Thôi! Đi xe đạp")
else:
    print("Không xác định")