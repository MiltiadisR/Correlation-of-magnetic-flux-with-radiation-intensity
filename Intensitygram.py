import matplotlib.pyplot as plt

import sunpy.map
from astropy.coordinates import SkyCoord
from astropy import units as u
from sunpy.net import Fido
from sunpy.net import attrs as a
result = Fido.search(a.Time('2020/12/11 20:25:00', '2020/12/11 20:26:00'),
                     a.Instrument.hmi, a.Physobs.intensity)
downloaded_file = Fido.fetch(result)
hmi_map = sunpy.map.Map(downloaded_file[0])
hmi_map.plot()
plt.show()
