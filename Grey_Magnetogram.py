import matplotlib.pyplot as plt
import sunpy.map
from sunpy.net import Fido
from sunpy.net import attrs as a
import xlwings as xw


wb = xw.Book('C:\\Users\\user\\Desktop\\Thesis\\ALL.xlsx')
sheet = wb.sheets['Sheet1']
i = 93
while i<127:
    result = Fido.search(a.Time(sheet.range((i+3,2)).value, sheet.range((i+3,3)).value),
                        a.Instrument.hmi, a.Physobs.los_magnetic_field)
    downloaded_file = Fido.fetch(result)
    print(downloaded_file)
    hmi_map = sunpy.map.Map(downloaded_file[0])
##    fig = plt.figure()
    hmi_rotated = hmi_map.rotate(order=3)
    hmi_rotated.plot()
    plt.show()
    i+=1
