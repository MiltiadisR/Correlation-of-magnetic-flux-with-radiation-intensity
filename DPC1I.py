from matplotlib import pyplot as plt

import sunpy.map
from sunpy.instr.aia import aiaprep
from sunpy.net import Fido, attrs as a

from astropy.coordinates import SkyCoord
from astropy import units as u

from astropy.io import fits
import numpy as np

import warnings
warnings.filterwarnings("ignore")
result = Fido.search(a.Time('2014-09-19T05:59:00', '2014-09-19T06:01:00'),
                     a.Instrument("aia"), a.Wavelength(193*u.angstrom),
                     a.vso.Sample(12*u.second))

file_download = Fido.fetch(result[0, 3], site='ROB')

# Define a region of interest
length = 250 * u.arcsec
x0 = 750 * u.arcsec #x position of the center
y0 = -400 * u.arcsec #y position of the center

# Create a SunPy Map, and a second submap over the region of interest.
smap = sunpy.map.Map(file_download[0])
bottom_left = SkyCoord(x0 - length, y0 - length,
                    frame=smap.coordinate_frame)
top_right = SkyCoord(x0 + length, y0 + length,
                    frame=smap.coordinate_frame)
submap = smap.submap(bottom_left, top_right=top_right)

fig = plt.figure(figsize=(5, 12))

# Create a second axis on the plot.
ax = fig.add_subplot(111, projection=submap) #plot is in the 1,2,2 position
submap.plot()
submap.draw_grid(grid_spacing=10*u.deg)
# Change the title.
ax.set_title('Zoomed View')


##x=fig.savefig('Zoomed1.png')

plt.show()

##filename = input('Enter a FITS file to CSV-ize: ')
##output = input('What would you like to call your new file?: ')
##
##hdulist = fits.open(filename)
##scidata = hdulist[0].data

##np.savetxt(output,scidata, fmt='%d', delimiter=',')

hdu_list=fits.open(file_download[0])
hdu_list.info()
image_data=hdu_list[1].data
plt.plot(image_data)
plt.show()

import pandas
df=pandas.DataFrame(image_data)
print(df)

