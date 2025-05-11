import astropy.units as u
from sunpy.net import Fido, attrs
import sunpy.map

q = Fido.search(
    attrs.Time('2019-01-01T00:00:00', '2019-01-01T01:00:00'),
    attrs.Sample(1*u.h),
    attrs.Instrument('AIA'),
    attrs.Wavelength(193*u.angstrom))

file = Fido.fetch(q)
m = sunpy.map.Map(file)
m.peek()
