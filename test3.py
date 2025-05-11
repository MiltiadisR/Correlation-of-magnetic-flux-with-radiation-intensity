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

w=[193]
j = 0
wb = xw.Book('C:\\Users\\user\\Desktop\\Thesis\\ALL.xlsx')
sheet = wb.sheets['Sheet1']
while j < 127:
    
    length = 30 * u.arcsec
    x0 = sheet.range((j+2,4)).value * u.arcsec #x position of the center
    y0 = sheet.range((j+2,5)).value * u.arcsec #y position of the center

    for k in w:
        
        #Searching the data from the internet
        warnings.filterwarnings("ignore")
        result = Fido.search(a.Time(sheet.range(j+2,2).value,sheet.range(j+2,3).value),
                             a.Instrument("aia"),
                             a.Wavelength(k*u.angstrom),
                             a.vso.Sample(12*u.second))

        file_download = Fido.fetch(result[0, 3], site='ROB')
        smap = sunpy.map.Map(file_download[0])

        bottom_left = SkyCoord(x0 - length, y0 - length,
                            frame=smap.coordinate_frame)
        top_right = SkyCoord(x0 + length, y0 + length,
                            frame=smap.coordinate_frame)
        submap = smap.submap(bottom_left, top_right=top_right)
        
        MT=0
        STDEV=0
        p=0
        x=submap.data
        Max=np.max(x)
        Min=np.min(x)
        pixel2=0

        MT=np.average(x)
        STDEV=np.std(x)
        TT = 0
        
        #define the threshold
        threshold = MT + STDEV

        for a in range(len(x)):
            for b in range(len(x)):
                p+=1
                if x[a,b] > threshold:
                    TT+= x[a,b]
                    pixel2+=1

        total=MT*p
    
    j+=1
