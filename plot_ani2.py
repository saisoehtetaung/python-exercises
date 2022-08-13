import numpy as np;
import matplotlib.pyplot as plt;
import matplotlib.animation as animation;

x_len = 200;
y_range = [0,20];

fig = plt.figure();
ax = fig.add_subplot(1,1,1);
xs = list(range(0,200));
ys = [0] * x_len;
ax.set_ylim(y_range);

line , = ax.plot(xs,ys);

plt.title("Temperature Data");
plt.xlabel('Samples');
plt.ylabel('Temperature (deg C)');

def animate(self,ys):
    rand_val = np.random.random()*20;

    temp_c = round(rand_val,2);
    print(temp_c);
    ys.append(temp_c);

    ys = ys[-x_len:];

    line.set_ydata(ys);

    return line ,


ani = animation.FuncAnimation(
    fig,
    animate,
    fargs = (ys,),
    interval = 100,
    blit = True
);
plt.show();