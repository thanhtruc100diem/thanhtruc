# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:59:50 2024

@author: Student
"""
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))

if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm.")
    else:
        print("Phương trình vô nghiệm.")
else:
    x = -b / a
    print(f"Nghiệm của phương trình là x = {x}")