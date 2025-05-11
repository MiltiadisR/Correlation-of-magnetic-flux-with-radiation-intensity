import matplotlib.pyplot as plt

import sunpy.map
from astropy.coordinates import SkyCoord
from astropy import units as u
from sunpy.net import Fido
from sunpy.net import attrs as a
import xlwings as xw
import numpy as np
import math

j = 0
wb = xw.Book('C:\\Users\\user\\Desktop\\Thesis\\ALL.xlsx')
sheet = wb.sheets['Sheet1']

while j < 127:
    
    length = 225 * u.arcsec
    x0 = sheet.range((j+3,4)).value * u.arcsec #x position of the center
    y0 = sheet.range((j+3,5)).value * u.arcsec #y position of the center
    
    result = Fido.search(a.Time(sheet.range((j+3,2)).value,sheet.range((j+3,3)).value),
                         a.Instrument.hmi, a.Physobs.los_magnetic_field)
    downloaded_file = Fido.fetch(result)
    hmi_map = sunpy.map.Map(downloaded_file[0])

    bottom_left = SkyCoord(x0 - length, y0 - length,
                           frame=hmi_map.coordinate_frame)
    top_right = SkyCoord(x0 + length, y0 + length,
                         frame=hmi_map.coordinate_frame)
    submap = hmi_map.submap(bottom_left, top_right=top_right)

    x=submap.data
    i=0
    l=0
    y=0.50431
    p=0
    e=y*725*pow(10,5)
    Tot=0
    total2=0
    pixel2=0
    total3=0
    pixel3=0

    d = math.sqrt(pow(x0.value,2) + pow(y0.value,2))
    R = 960
    r=d/R
    μ=math.sqrt(1-pow(r,2))
    χ=x*μ
    submap.plot()
    plt.savefig('C:\\Users\\user\\Desktop\\Thesis\\NEW\\HMI\\LOS\\'
                    +str(sheet.range((j+3,2)).value.year)+'-'
                    +str(sheet.range((j+3,2)).value.month)+'-'
                    +str(sheet.range((j+3,2)).value.day)+' '
                    +'HMI '
                    +str(int(sheet.range((j+3,7)).value))+'.png')

##    for i in range(len(χ)-3):
##        for l in range(len(χ)-3):
##            Tot+=abs(χ[i,l]*μ)*pow(e,2)
##            p+=1
##            if abs(χ[i,l]) > 100 and abs(χ[i,l])<1000:
##                total2+=abs(χ[i,l]*μ)*pow(e,2)
##                pixel2+=1
##                
##
##    sheet.range((j+3,15)).value = Tot
##    sheet.range((j+3,16)).value = p
##    sheet.range((j+3,17)).value = total2
##    sheet.range((j+3,18)).value = pixel2
##    sheet.range((j+3,11)).value = total3
##    sheet.range((j+3,12)).value = pixel3
    
    ##    for i in range(len(x)):
##        for l in range(len(x)):
##            if abs(x[i,l]*μ) > 100:
##                total3+=abs(x[i,l]*μ)*pow(e,2)
##                pixel3+=1
                
    
##    print('The Total Unsigned Magnetic Flux =',Tot,'Mx')
    j+=1
