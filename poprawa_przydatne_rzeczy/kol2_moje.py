import pandas as pd
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
from scipy.integrate import quad
#Zadanie 1
df = pd.read_csv('data.csv')

#Zadanie 2
print(df)
df.dropna(0, inplace=True)
print(df)

#Zadanie 3
x1 = df['x'].values
y1 = df['y'].values

f_interp = interp1d(x1,y1,kind='quadratic')

#Zadanie 4
f_quad = quad(f_interp,0,2)
print(f_quad)


#Zadanie 5
plt.plot(x1, y1, 'v', color="green", label='data points', lw=1.5)
plt.plot(x1, f_interp(x1), '-', color="black", label='interpolation')

plt.xlabel('x')
plt.ylabel('y')
plt.title('interpolation')
plt.legend(loc=3)

plt.grid()
plt.savefig('interpolation.png')
plt.show()