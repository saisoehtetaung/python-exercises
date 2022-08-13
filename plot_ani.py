import datetime as dt;
import numpy as np;
import matplotlib.pyplot as plt;
import matplotlib.animation as ani;

fig = plt.figure();
ax = fig.add_subplot(1,1,1);
xs = [];
ys = [];

def animate(i,xs,ys):
    temp_c = round(np.random.random(),2);

    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'));
    ys.append(temp_c);

    xs = xs[-20:];
    ys = ys[-20:];

    ax.clear();
    ax.plot(xs,ys);

    plt.xticks(rotation = 45, ha = 'right');
    plt.subplots_adjust(bottom=0.3);
    plt.title("Temperature Data");
    plt.ylabel("Temperature (deg C)");


ani = ani.FuncAnimation(fig, animate, fargs=(xs,ys), interval=1000);
plt.show();