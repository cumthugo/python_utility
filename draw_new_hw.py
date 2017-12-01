import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('temp_new_hw.txt')
#print(data)
from scipy.optimize import curve_fit

temp = data[:,0]
R = data[:,1]
voltage_calc = R*5/(R+10)
voltage_acu = data[:,2]
voltage = voltage_acu

x = np.arange(111)

temp_param = np.polyfit(voltage,temp,7)
print(temp_param)
temp_func = np.poly1d(temp_param)
print(temp_func)
temp_calc = temp_func(voltage)

def calc_R(x,a,b,c):
    return a / (b - x) + c;

#print(voltage)
plt.subplot(211)
plt.plot(voltage,temp,'o')
plt.plot(voltage,temp_calc,'r')
plt.xlabel('Voltage (V)')
plt.ylabel(r'Temerature $^{\circ}$C')
plt.subplot(212)
'''
plt.plot(x,voltage_calc,'r')
plt.plot(x,voltage_acu,'b')
plt.legend(['Theory Voltage','Actual Voltage'])
'''
popt,pcov = curve_fit(calc_R,voltage,R,bounds=([0,4.79,-1000],[100.,8.,1000]))
print(popt)

plt.plot(voltage_acu,R,'b')
plt.plot(voltage_acu,calc_R(voltage_acu,*popt),'r')

plt.xlabel('Voltage (V)')
plt.ylabel(r'Resistance k$\Omega$')
#plt.xlimit(0,5)
plt.show()

