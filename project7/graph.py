
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.transform import Rotation as Rot
import time


plt.cla()
# for stopping simulation with the esc key.
plt.gcf().canvas.mpl_connect('key_release_event',
        lambda event: [exit(0) if event.key == 'escape' else None])




# plotting lattitude/longitude ratio graph
x=[1,2,3,4,5,6]
y=[1,2,3,4,5,6]

for i in range(6):


    plt.plot(x[i], y[i], ".g")
    time.sleep(2) # increment every 2 second
    plt.grid(True)
    plt.pause(0.1)



   