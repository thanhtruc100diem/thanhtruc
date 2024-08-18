# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 09:11:48 2024

@author: Student
"""

a=float(input(" Nhập hệ số a: "))
b=float(input(" Nhập hệ số b: "))
c=float(input(" Nhập hệ số c: "))
if a+b>c and a+c>b and c+b>a:
        print("a,b,c có thể là ba cạnh của một tam giác.")
else:
        print("a,b,c không phải ba cạnh của một tam giác.")
