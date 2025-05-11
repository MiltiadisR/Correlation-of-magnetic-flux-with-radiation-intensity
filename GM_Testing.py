import matplotlib.pyplot as plt

import sunpy.map
from astropy.coordinates import SkyCoord
from astropy import units as u
from sunpy.net import Fido
from sunpy.net import attrs as a
result = Fido.search(a.Time('2010/11/29 23:01:00', '2010/11/29 23:02:00'),
                     a.Instrument.hmi, a.Physobs.los_magnetic_field)
downloaded_file = Fido.fetch(result)
print(downloaded_file)
# Define a region of interest
length = 50 * u.arcsec
x0 = 240 * u.arcsec #x position of the center
y0 = 220 * u.arcsec #y position of the center

# Create a SunPy Map, and a second submap over the region of interest.
hmi_map = sunpy.map.Map(downloaded_file[0])
hmi_rotated = hmi_map.rotate(order=3)
bottom_left = SkyCoord(x0 - length, y0 - length,
                    frame=hmi_map.coordinate_frame)
top_right = SkyCoord(x0 + length, y0 + length,
                    frame=hmi_map.coordinate_frame)
submap = hmi_rotated.submap(bottom_left, top_right=top_right)

# Create a new matplotlib figure, larger than default.
fig = plt.figure(figsize=(5, 12))

# Add a first Axis, using the WCS from the map.
ax1 = fig.add_subplot(1, 2, 1, projection=hmi_rotated) #plot is in the 1,2,1 position

# Plot the Map on the axes with default settings.
hmi_rotated.plot()

# Draw a box on the image
hmi_rotated.draw_rectangle(bottom_left, height=length * 2, width=length * 2)

# Create a second axis on the plot.
ax2 = fig.add_subplot(1, 2, 2, projection=submap) #plot is in the 1,2,2 position

submap.plot()

# Add a overlay grid.
submap.draw_grid(grid_spacing=10*u.deg)

# Shows the plot
plt.show()
##hmi_rotated = hmi_map.rotate(order=3)
##hmi_rotated.plot()
##plt.show()
##submap.plot()
##
##submap.draw_grid(grid_spacing=10*u.deg)
##plt.show()

x=submap.data
a=0
y=0
Max=0
i=0
j=0

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

MT=sum1/len(x)

print('Η μέση τιμή είναι:',MT)

sum2=0

for i in range(len(x)):
	for j in range(len(x)):
		D=x[i,j]-MT
		sum2+=pow(D,2)

o=sum2/(len(x)-1)
s=pow(o,0.5)

print('Το σφάλμα είναι:',s)
print(MT,'±',s)


