from matplotlib import pyplot as plt

import sunpy.map
from sunpy.instr.aia import aiaprep
from sunpy.net import Fido, attrs as a

from astropy.coordinates import SkyCoord
from astropy import units as u

from astropy.io import fits
import numpy as np

import warnings

#Searching the data from the internet
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

# Create a new matplotlib figure, larger than default.
fig = plt.figure(figsize=(5, 12))

# Add a first Axis, using the WCS from the map.
ax1 = fig.add_subplot(1, 2, 1, projection=smap) #plot is in the 1,2,1 position

# Plot the Map on the axes with default settings.
smap.plot()

# Draw a box on the image
smap.draw_rectangle(bottom_left, height=length * 2, width=length * 2)

# Create a second axis on the plot.
ax2 = fig.add_subplot(1, 2, 2, projection=submap) #plot is in the 1,2,2 position

submap.plot()

# Add a overlay grid.
submap.draw_grid(grid_spacing=10*u.deg)

# Change the title.
ax2.set_title('Zoomed View')

# Shows the plot
plt.show()

# Define the valuables
x=submap.data
a=0
y=0
Max=0
i=0
j=0

# Read all the data and saving the maximum
for i in range(len(x)):
    for j in range(len(x)):
        if x[i,j]>a:
            y=x[i,j]
            Max=y
            a=Max

print('Το μέγιστο είναι:',Max)

sum1=0

for i in range(len(x)):
    for j in range(len(x)):
        sum1+=x[i,j]

MT=sum1/pow(len(x),2)

print('Η μέση τιμή είναι:',MT)

sum2=0

for i in range(len(x)):
	for j in range(len(x)):
		D=x[i,j]-MT
		sum2+=pow(D,2)

o=sum2/(pow(len(x),2)-1)
s=pow(o,0.5)

print('Το σφάλμα είναι:',s)
print(MT,'±',s)
