# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:41:37 2024

@author: Student
"""

x= float (input("Nhập điểm trung bình:"))
if x <  3.5:
    print("Học lực kém")
elif 3.5 <= x < 5:
    print("Học lực yếu")
elif 5 <= x < 7 :
    print ("Học lực trung bình")
elif 7 <= x < 8:
    print ("Học lực khá")
elif 8 <= x < 9:
    print ("Học lực giỏi")
elif 9<= x <= 10:
    print ("Học lực xuất sắc")
else:
    print("Khong xác định")