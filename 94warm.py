import numpy as np
import xlwings as xw
import math
wb = xw.Book('C:\\Users\\user\\Desktop\\Thesis\\ALL.xlsx')
sheet = wb.sheets['Sheet1']

a=[-0.0731,0.975,0.099,-0.00284]
f=0.31
I94warm = 0

j = 0
while j < 127:
    
    I171 = sheet.range((j+3,51)).value
    I193 = sheet.range((j+3,76)).value

    for i in range(len(a)):
        I94 = 0.39*a[i]*pow(((f*I171 + (1-f)*I193)/116.54),i)

        I94warm +=I94
##    I1 = 0.39*a[0]*pow(((f*I171 + (1-f)*I193)/116.54),0)
##    I2 = 0.39*a[1]*pow(((f*I171 + (1-f)*I193)/116.54),1)
##    I3 = 0.39*a[2]*pow(((f*I171 + (1-f)*I193)/116.54),2)
##    I4 = 0.39*a[3]*pow(((f*I171 + (1-f)*I193)/116.54),3)
##    I94warm = I1+I2+I3+I4
    sheet.range((j+3,99)).value = I94warm


    j+=1

    
