# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 09:24:43 2024

@author: Student
"""

a=float(input(" Nhập hệ số a: "))
b=float(input(" Nhập hệ số b: "))
c=float(input(" Nhập hệ số c: "))
if a+b>c and a+c>b and b+c>a:
    
    if a==b==c:
        print("Tam giác đều.")
    elif a==b or a==c or b==c:
        print( "Tam giác cân.")  
    if a**2 + b**2 == c**2 or b**2 + c**2== a**2 or a**2 + c**2 == b**2:
        print("Tam giác vuông.")
else:
    print("Không xác định.")