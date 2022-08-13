import numpy as np;
import matplotlib.pyplot as plt;

xstart = 0;
xstop = 2*np.pi;
increment = 0.1;

x = np.arange(xstart,xstop,increment);
y= np.sin(x);
z= np.cos(x);

plt.subplot(2,1,1);
plt.plot(x,y,"g");
plt.title("sin(x)");
plt.grid(); 
plt.xlabel('x');
plt.ylabel('y');
plt.show();

plt.subplot(2,1,2);
plt.plot(x,z,"r");
plt.title("cos(x)");
plt.grid(); 
plt.xlabel('x');
plt.ylabel('y');
plt.show();

print(np.zeros(10));
