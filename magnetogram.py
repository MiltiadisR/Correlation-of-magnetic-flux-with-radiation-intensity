from matplotlib import pyplot as plt

import sunpy.map
from sunpy.instr.aia import aiaprep
from sunpy.net import Fido, attrs as a

from astropy.coordinates import SkyCoord
from astropy import units as u

import warnings
warnings.filterwarnings("ignore")
result = Fido.search(a.Time('2014-09-19T05:59:00', '2014-09-19T06:01:00'),
                     a.Instrument("aia"), a.Wavelength(193*u.angstrom),
                     a.vso.Sample(12*u.second))
file_download = Fido.fetch(result[0, 3], site='ROB')
aia1 = sunpy.map.Map(file_download[0])
aia = aiaprep(aia1)
plt.rc('font',family='serif')
plt.figure(figsize=[8,10])
aia.plot()
aia.draw_limb()
plt.grid(True)
plt.show()

# το κατω δεν χρειαζεται
#mapc=sunpy.map.Map(cube=True)
#mapc=sunpy.map.Map([amap.submap([-1200,-500],[-200,700]) for amap in mapc.mapc],cube=True)
#fig = plt.figure(figsize=(10,12))
#ani = mapc.plot()
#ani.save("test.mp4", bitrate=5000)
#plt.close()
