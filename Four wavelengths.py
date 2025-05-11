from matplotlib import pyplot as plt
import sunpy.map
from sunpy.instr.aia import aiaprep
from sunpy.net import Fido, attrs as a
from astropy.coordinates import SkyCoord
from astropy import units as u
from astropy.io import fits
import numpy as np
import warnings
import xlwings as xw
import math

w=[94,171,193,211]
j = 93
wb = xw.Book('C:\\Users\\user\\Desktop\\Thesis\\ALL.xlsx')
sheet = wb.sheets['Sheet1']
while j < 127:
    
##    length = sheet.range((j+3,6)).value * u.arcsec
    length = 225 * u.arcsec
    x0 = sheet.range((j+3,4)).value * u.arcsec #x position of the center
    y0 = sheet.range((j+3,5)).value * u.arcsec #y position of the center

    for k in w:

        #Searching the data from the internet
        warnings.filterwarnings("ignore")
        result = Fido.search(a.Time(sheet.range((j+3,2)).value,sheet.range((j+3,3)).value),
                             a.Instrument("aia"),
                             a.Wavelength(k*u.angstrom),
                             a.vso.Sample(12*u.second))

        file_download = Fido.fetch(result[0, 3], site='ROB')
        smap = sunpy.map.Map(file_download[0])
        smap.plot()
        plt.show()

        bottom_left = SkyCoord(x0 - length, y0 - length,
                            frame=smap.coordinate_frame)
        top_right = SkyCoord(x0 + length, y0 + length,
                            frame=smap.coordinate_frame)
        submap = smap.submap(bottom_left, top_right=top_right)

        p=0
        x=submap.data
        d = math.sqrt(pow(x0.value,2) + pow(y0.value,2))
        R = 960
        r=d/R
        μ=math.sqrt(1-pow(r,2))
        χ=x*μ
        print(χ[200,250],k)
        
        Max=np.max(χ)
        Min=np.min(χ)
        pixel2=0

        MT=np.average(χ)
        STDEV=np.std(χ)
        TT = 0
        TTT=0
        
        #define the threshold
        threshold = MT + STDEV
##        plt.imshow(χ,cmap='sdoaia193')
##        plt.savefig('C:\\Users\\user\\Desktop\\Thesis\\NEW\\193\\LOS\\'
##                    +str(sheet.range((j+3,2)).value.year)+'-'
##                    +str(sheet.range((j+3,2)).value.month)+'-'
##                    +str(sheet.range((j+3,2)).value.day)+' '
##                    +str(k)+'A '
##                    +str(int(sheet.range((j+3,7)).value))+'.png')
##        
##        c=plt.imshow(χ,cmap='sdoaia193',vmin=threshold)
##        plt.colorbar(c)
##        plt.savefig('C:\\Users\\user\\Desktop\\Thesis\\NEW\\193\\LOS\\'
##                    +str(sheet.range((j+3,2)).value.year)+'-'
##                    +str(sheet.range((j+3,2)).value.month)+'-'
##                    +str(sheet.range((j+3,2)).value.day)+' '
##                    +str(k)+'A TT '
##                    +str(int(sheet.range((j+3,7)).value))+'.png')
##        
##        plt.show()
        for i in range(len(χ)-3):
            for l in range(len(χ)-4):
                p+=1
                if χ[i,l] > threshold:
                    TT+= χ[i,l]
                    pixel2+=1
                    TTT+=χ[0,0]


##        print(TTT,k)
##        total=MT*p
##        
##        sheet.range((j+3,70)).value = MT
##        sheet.range((j+3,71)).value = STDEV
##        sheet.range((j+3,72)).value = total
##        sheet.range((j+3,73)).value = p
##        sheet.range((j+3,74)).value = Max
##        sheet.range((j+3,75)).value = Min
##        sheet.range((j+3,76)).value = TT
##        sheet.range((j+3,77)).value = pixel2
        
##    print('Η μέση τιμή είναι:',MT
##          ,'Η τυπική απόκλιση είναι:',STDEV
##          ,'Ο αριθμός των pixel είναι:',p
##          ,'Η μέγιστη τιμή είναι:',Max
##          ,'Η ελάχιστη τιμή είναι:',Min,sep='\n')
##    print(sheet.range((j+3,2)).value)
##    print(MT,STDEV,total,p,Max,Min,TT,pixel2,sep='\t')
    j+=1



    
