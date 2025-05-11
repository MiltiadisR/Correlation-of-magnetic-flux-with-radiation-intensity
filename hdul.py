from astropy.io import fits
from matplotlib import pyplot as plt

hdu_list=fits.open("C:\\Users\\user\\sunpy\\data\\aia_20151023_231046_0211_image_lev1.fits")
hdu_list.info()
##image_data=hdu_list[1].data
##print(type(image_data))
##print(image_data.shape)

##plt.imshow(image_data)
##plt.show
print(hdu_list[1].header)

print(hdu_list[1].header['CDELT1'])
print(hdu_list[1].header['CDELT2'])

hdu_list[1].header['EXPTIME']
