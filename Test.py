from matplotlib import pyplot as plt
import sunpy.map
from sunpy.instr.aia import aiaprep
from sunpy.net import Fido, attrs as a
from astropy.coordinates import SkyCoord
from astropy import units as u
from astropy.io import fits
import numpy as np
import warnings
from datetime import datetime

w=[94,171,193,211]
y = int(input('Year:'))
mo = int(input('Month:'))
d = int(input('Day:'))
h = int(input('Hour:'))
mi = int(input('Minute:'))
strt = datetime(y,mo,d,h,mi,00)
fin = datetime(y,mo,d,h,mi+1,00)

warnings.filterwarnings("ignore")
result = Fido.search(a.Time(strt,fin),
                     a.Instrument("aia"), a.Wavelength(193*u.angstrom),
                     a.vso.Sample(12*u.second))

file_download = Fido.fetch(result[0, 3], site='ROB')
smap = sunpy.map.Map(file_download[0])
smap.plot()
plt.show()
