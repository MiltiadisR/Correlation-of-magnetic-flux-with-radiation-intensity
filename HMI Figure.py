import matplotlib.pyplot as plt
import sunpy.map
from astropy.coordinates import SkyCoord
from astropy import units as u
from sunpy.net import Fido
from sunpy.net import attrs as a

import warnings

warnings.filterwarnings("ignore")
result = Fido.search(a.Time('2012/07/30 20:26:00', '2012/07/30 20:27:00'),
                     a.Instrument.hmi, a.Physobs.los_magnetic_field)
downloaded_file = Fido.fetch(result)
hmi_map = sunpy.map.Map(downloaded_file[0])

length = 50 * u.arcsec
x0 = -230 * u.arcsec #x position of the center
y0 = -400 * u.arcsec #y position of the center

bottom_left = SkyCoord(x0 - length, y0 - length,
                    frame=hmi_map.coordinate_frame)
top_right = SkyCoord(x0 + length, y0 + length,
                    frame=hmi_map.coordinate_frame)
submap = hmi_map.submap(bottom_left, top_right=top_right)

submap.plot()

##submap.draw_grid(grid_spacing=10*u.deg)
plt.show()

##plt.savefig('C:\\Users\\user\\Desktop\\Thesis\\Images\\2019-05-11 HMI.png')
