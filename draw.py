import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('temp.txt')
#print(data)

temp = data[:,0]
R = data[:,1]
voltage = R*5/(R+10)


temp_param = np.polyfit(voltage,temp,7)
print(temp_param)
temp_func = np.poly1d(temp_param)
print(temp_func)
temp_calc = temp_func(voltage)

#print(voltage)
plt.plot(voltage,temp,'o')
plt.plot(voltage,temp_calc,'r')
plt.xlabel('Voltage (V)')
plt.ylabel('Temerature C')
#plt.xlimit(0,5)

plt.show()

