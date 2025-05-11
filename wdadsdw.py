import numpy as np
import xlwings as xw
import math
wb = xw.Book('C:\\Users\\user\\Desktop\\Thesis\\ALL.xlsx')
sheet = wb.sheets['Sheet1']

a=[-0.0731,0.975,0.099,-0.00284]
f=0.31
I94warm = 0


I171 = 1300
I193 = 2200

for i in range(len(a)):
    I94 = 0.39*a[i]*pow(((f*I171 + (1-f)*I193)/116.54),i)

    I94warm +=I94

print(I94warm)
