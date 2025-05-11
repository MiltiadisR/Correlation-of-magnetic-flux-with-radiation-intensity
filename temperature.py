import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from scipy.stats import pearsonr

x=[6.8,6.3,6.2,5.8]
##x=[94,211,193,171]
y=[0.81283282,0.41589355,0.57613334,0.57283567]
plt.plot(x,y,'ro')
plt.plot(6.8,0.65853907,'bx')
plt.ylabel("Correlation Coefficient")
plt.xlabel("LOG10(T)") 
plt.show()
