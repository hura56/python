import pandas as pd
import matplotlib.pyplot as plt
import numpy
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
#fig, (ax1,ax2) = plt.subplots(1,2)
#fig.subplots_adjust(hspace=0.5)
y1 = [35,25,27,10,33,12]
x = ['Styczeń','Luty','Marzec','Kwiecień','Maj','Czerwiec']
#color1 = 'lightblue', 'pink', 'orange', 'grey', 'purple'
plt.bar(x,y1, color='yellow', label='X')
plt.title('Wykres zmian X i Y')
y2 = [-12,-18,-11,-10,-11,-15]
#color2 = 'hotpink', 'turquoise', 'turquoise', 'saddlebrown', 'yellow'
plt.bar(x,y2, color='saddlebrown', label='Y')
plt.legend()
plt.xticks(rotation=30)
#plt.title('Wykres prawy')
#plt.major_locator(MultipleLocator(20))
plt.show()