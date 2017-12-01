import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('temp_new_hw_0831.txt')
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

def calc_temp_new(R,Rin):
    return (5 * R * Rin) / (R*Rin + 10 * R + 10 * Rin)

#print(voltage)



def calc_v2(R2,R4,R5):
    R1 = 10
    R3 = 39
    return (5*R2*R3*R4*R5 + 5*R3*R5*(R1*R2+R1*R3+R2*R3)) / ((R1*R2+R2*R3+R1*R3)*(R3*R4+R3*R5+R4*R5) - R1*R2*R4*R5)


popt,pcov = curve_fit(calc_v2,R,voltage,bounds=([1,1],[999999999,9999999999]))
print(popt) 
plt.plot(R,voltage,'o')
plt.plot(R,calc_v2(R,*popt),'r')
plt.show()

v2 = calc_v2(R,*popt)
for v in v2:
    print("%.2f\n"%(v))
    

'''
plt.subplot(211)
plt.plot(voltage,temp,'o')
plt.plot(voltage,temp_calc,'r')
plt.xlabel('Voltage (V)')
plt.ylabel(r'Temerature $^{\circ}$C')


R_popt,R_pcov = curve_fit(calc_temp_new,R,voltage,bounds=(10,99999))

print('haha')
print(R_popt)

plt.subplot(212)



popt,pcov = curve_fit(calc_R,voltage,R,bounds=([0,4.79,-1000],[100.,8.,1000]))
print(popt)

R_new = (10 * voltage) / ( 5 - voltage)
plt.plot(voltage_acu,R,'b')
plt.plot(voltage_acu,calc_R(voltage_acu,*popt),'r')
plt.plot(voltage_acu,R_new,'g')

plt.xlabel('Voltage (V)')
plt.ylabel(r'Resistance k$\Omega$')
#plt.xlimit(0,5)
plt.show()
'''
