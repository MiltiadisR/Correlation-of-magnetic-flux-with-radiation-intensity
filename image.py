from __future__ import print_function, division                             
import matplotlib.pyplot as plt                     
import sunpy.map                    
from sunpy.data.sample import AIA_193_IMAGE
import numpy as np                             
import matplotlib.pylab as plt

smap = sunpy.map.Map(AIA_193_IMAGE)
sizes = np.shape(smap.data)     
fig = plt.figure()
fig.set_size_inches(1. * sizes[0] / sizes[1], 1, forward = False)
ax = plt.Axes(fig, [0., 0., 1., 1.])
ax.set_axis_off()
fig.add_axes(ax)
ax.imshow(smap.data, norm=smap.plot_settings['norm'], cmap=smap.plot_settings['cmap'], origin='lower')
plt.savefig('test_image.png', dpi = sizes[0]) 
#plt.close()
plt.show()
