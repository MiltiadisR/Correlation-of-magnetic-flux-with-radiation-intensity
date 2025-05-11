from matplotlib import pyplot as plt
import sunpy.map
from sunpy.instr.aia import aiaprep
from sunpy.net import Fido, attrs as a
from astropy.coordinates import SkyCoord
from astropy import units as u
from astropy.io import fits
import numpy as np
import warnings

w=[211]

length = 60 * u.arcsec
x0 = -230 * u.arcsec #x position of the center
y0 = -400 * u.arcsec #y position of the center

for k in w:
    #Searching the data from the internet
    warnings.filterwarnings("ignore")
    result = Fido.search(a.Time('str(strt)', 'str(fin)'),
                         a.Instrument("aia"), a.Wavelength(k*u.angstrom),
                         a.vso.Sample(12*u.second))

    file_download = Fido.fetch(result[0, 3], site='ROB')
    smap = sunpy.map.Map(file_download[0])

    bottom_left = SkyCoord(x0 - length, y0 - length,
                        frame=smap.coordinate_frame)
    top_right = SkyCoord(x0 + length, y0 + length,
                        frame=smap.coordinate_frame)
    submap = smap.submap(bottom_left, top_right=top_right)

    submap.plot()
    submap.draw_grid(grid_spacing=10*u.deg)

    # plt.savefig('C:\\Users\\user\\Desktop\\Thesis\\Images\\2012-07-30 '+str(k)+
    #             'A.png')
    plt.show()
    
    MT=0
    STDEV=0
    p=0
    x=submap.data
    Max=np.max(x)
    Min=np.min(x)

    MT=np.average(x)
    STDEV=np.std(x)
    for i in range(len(x)):
        for j in range(len(x)):
            p+=1

    print('Η μέση τιμή είναι:',MT,'Η τυπική απόκλιση είναι:',STDEV,'Ο αριθμός των pixel είναι:',p,'Η μέγιστη τιμή είναι:',Max,'Η ελάχιστη τιμή είναι:',Min,sep='\n')
    print(MT,STDEV,p,Max,Min,sep='\t')
