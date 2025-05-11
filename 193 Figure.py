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
result = Fido.search(a.Time('2019/05/11 20:25:00', '2019/05/11 20:26:00'),
                     a.Instrument("aia"), a.Wavelength(193*u.angstrom),
                     a.vso.Sample(12*u.second))

file_download = Fido.fetch(result[0, 3], site='ROB')
smap = sunpy.map.Map(file_download[0])

# Plot the Map on the axes with default settings.
smap.plot()

plt.savefig('C:\\Users\\user\\Desktop\\Thesis\\Images\\2019-05-11 193.png')
