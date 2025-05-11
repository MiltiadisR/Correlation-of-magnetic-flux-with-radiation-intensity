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

##hdu_list=fits.open(downloaded_file[0])
##
###Define The Center
##c=[hdu_list[1].header['CRPIX1'],hdu_list[1].header['CRPIX2']]
##
##submap.fits_header

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

## Corect LoS Magnetic field
χ=x*μ

##plt.imshow(x,cmap='sdoaia211',vmin=threshold)

fig, axes = plt.subplots(ncols=2, figsize=(8, 3))
ax = axes.ravel()

ax[0].imshow(χ,cmap=plt.cm.gray,vmin=-1000,vmax=1000)
ax[0].set_title('Original image')

ax[1].imshow(χ,cmap=plt.cm.gray,vmax=1000)
ax[1].set_title('Result')

plt.show()

from skimage.filters import threshold_otsu


thresh = threshold_otsu(χ)
binary = χ > -100
binary2 = binary<100


fig, axes = plt.subplots(ncols=3, figsize=(8, 2.5))
ax = axes.ravel()
ax[0] = plt.subplot(1, 3, 1)
ax[1] = plt.subplot(1, 3, 2)
ax[2] = plt.subplot(1, 3, 3, sharex=ax[0], sharey=ax[0])

ax[0].imshow(χ, cmap=plt.cm.gray)
ax[0].set_title('Original')
ax[0].axis('off')

ax[1].hist(χ.ravel())
ax[1].set_title('Histogram')
ax[1].axvline(thresh, color='r')

ax[2].imshow(binary2, cmap=plt.cm.gray)
ax[2].set_title('Thresholded')
ax[2].axis('off')

plt.show()

