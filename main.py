import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from air_cl import Air
from space_cl import Space
from air_cl import Particle, resy, resx

dim = 0.01


# Initialize Space
space = Space(dim, dim, 10000)
space.setmol()
space.setmaxwell()
space.update()

# Get initial scatter data
bxscat = space.getscatx()
byscat = space.getyscat()

# Create figure and axis
fig, ax = plt.subplots()
fig2, ax2 = plt.subplots()
ax2.set_xlim(0, dim)
ax2.set_ylim(0, dim)


sc = ax.scatter(bxscat, byscat)
he = ax.scatter(space.get_he_cord()[0], space.get_he_cord()[1], color = "red")

pl = ax2.scatter(resx, resy)

# Update function for animation
def update(frame):
    space.update()  # Update molecule positions
    bxscat = space.getscatx()  # Get updated x coordinates
    byscat = space.getyscat()  # Get updated y coordinates
    sc.set_offsets(np.c_[bxscat, byscat])  # Update scatter plot data
    he.set_offsets(np.c_[space.get_he_cord()[0], space.get_he_cord()[1]])
    pl.set_offsets(np.c_[resx, resy])

    return sc, he, pl

# Initialize function (not necessary in this case since we update the plot in the first frame)
def init():
    return sc,


frame_rate = 30  # frames per second
duration = 15  # seconds
total_frames = frame_rate * duration
# Create animation
for i in range (1):
    ani = animation.FuncAnimation(fig, update, frames=total_frames, init_func=init, blit=True)
    ani2 = animation.FuncAnimation(fig2, update, frames=total_frames, init_func=init, blit=True)
    #ani = animation.FuncAnimation(fig, update, frames=100, init_func=init, blit=True)
    ax2.scatter(resx, resy)
    plt.show()

# Display animation
