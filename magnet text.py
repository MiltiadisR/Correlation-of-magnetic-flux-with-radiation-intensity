import matplotlib.pyplot as plt

import sunpy.map
from astropy.coordinates import SkyCoord
from astropy import units as u
from sunpy.net import Fido
from sunpy.net import attrs as a
import xlwings as xw
import numpy as np
from astropy.io import fits
import math

j = 0
wb = xw.Book('C:\\Users\\user\\Desktop\\Thesis\\ALL.xlsx')
sheet = wb.sheets['Sheet1']
    
length = 200 * u.arcsec
x0 = sheet.range((j+2,4)).value * u.arcsec #x position of the center
y0 = sheet.range((j+2,5)).value * u.arcsec #y position of the center
    
result = Fido.search(a.Time(sheet.range((j+2,2)).value,sheet.range((j+2,3)).value),
                     a.Instrument.hmi, a.Physobs.los_magnetic_field)

downloaded_file = Fido.fetch(result)

hmi_map = sunpy.map.Map(downloaded_file[0])
bottom_left = SkyCoord(x0 - length, y0 - length,
                       frame=hmi_map.coordinate_frame)
top_right = SkyCoord(x0 + length, y0 + length,
                     frame=hmi_map.coordinate_frame)
submap = hmi_map.submap(bottom_left, top_right=top_right)

##hdu_list=fits.open(downloaded_file[0])
##
###Define The Center
##c=[hdu_list[1].header['CRPIX1'],hdu_list[1].header['CRPIX2']]
##
##submap.fits_header

d = math.sqrt(pow(x0.value,2) + pow(y0.value,2))
R = 960
r=d/R
μ=math.sqrt(1-pow(r,2))
