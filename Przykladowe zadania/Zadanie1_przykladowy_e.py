import pandas as pd
import matplotlib.pyplot as plt
import numpy
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
fig, (ax1,ax2) = plt.subplots(1,2)
#fig.subplots_adjust(hspace=0.5)
y1 = [35,47,15,40,39]
x = ['A','B','C','D','E']
color1 = 'lightblue', 'pink', 'orange', 'grey', 'purple'
ax1.barh(x,y1, align='center', color=color1)
ax1.xaxis.set_major_locator(MultipleLocator(10))
ax1.set_title('Wykres lewy')

y2 = [-30,-32,-38,-35,-28]
color2 = 'hotpink', 'turquoise', 'turquoise', 'saddlebrown', 'yellow'
ax2.barh(x,y2, align='center', color=color2)
ax2.set_title('Wykres prawy')

plt.show()