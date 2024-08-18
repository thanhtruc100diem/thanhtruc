# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 08:28:46 2024

@author: Student
"""
import math
a= float(input("Nhập hệ số a: "))
b= float( input("Nhập hệ số b: "))
c= float(input(" Nhập hệ số c: "))
delta = b**2 - 4*a*c
if a == 0:
    if b ==0:
        if c ==0:
            print(" Phương trình có vô số nghiệm.")
        else :
            print(" Phương trình có vô nghiệm.")
    else:
          x = -c / b
          print(f"Nghiệm của phương trình là x = {x}")
else:
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Phương trình có hai nghiệm phân biệt: x1 = {x1} và x2 = {x2}")
    elif delta == 0:
        x = -b / (2 * a)
        print(f"Phương trình có nghiệm kép: x = {x}")
    else:
        print("Phương trình vô nghiệm.")
        
