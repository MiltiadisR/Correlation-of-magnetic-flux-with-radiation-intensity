import matplotlib.pyplot as plt
import numpy as np
import xlwings as xw
from sklearn.linear_model import LinearRegression
from scipy.stats import pearsonr

wb = xw.Book('C:\\Users\\user\\Desktop\\Thesis\\ALL.xlsx')
sheet = wb.sheets['Sheet1']
x = sheet.range('Q3:Q123').value
y = sheet.range('DH3:DH123').value

PHI=np.log10(x)
I=np.log10(y)

coeff,cov = np.polyfit(PHI,I,1, cov=True)    #Shows slope and intercept
r, p = pearsonr(PHI,I)  #corelation coefficient and p-values

dfit = np.sqrt(np.diag(cov))
##plt.xscale('log')
##plt.yscale('log')
plt.xlabel("Log Total Unsighed Magnetic Flux (Mx)")
plt.ylabel("Log Total Intensity 94A Hot(DN/s)")
##formatter0 = EngFormatter(unit='Mx')

#PHI = m*I + b
m=coeff[0]
b=coeff[1]
#Plot the trnd line
PHItrend = np.linspace(min(PHI),max(PHI),100)
Itrend = m*PHItrend + b

plt.plot(PHI,I,'.', label="data")
plt.plot(PHItrend,Itrend,'r-',zorder=-1, label="m*PHI+b")
plt.text(min(PHI)-0.05, max(I)-0.55, "m={0:0.2f} ± {1:0.2f} \nb={2:0.2f} ± {3:0.2f}"
         .format(m,dfit[0],b,dfit[1]), fontsize=12)
plt.legend(loc="upper left")

print(np.corrcoef(PHI,I))
print(coeff)
print(np.sqrt(np.diag(cov)))
print('P-Value:',p)
plt.show()
