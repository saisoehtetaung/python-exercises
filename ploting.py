import numpy as np;
import matplotlib.pyplot as plt;

plt.axis([0,20,0,1]);

delay= 1;
for i in range(10):
    y = np.random.random();
    plt.scatter(i,y);
    plt.pause(delay);

plt.show();