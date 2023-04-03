import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Compute orbit

t = 0
dt = float(input("Insert the timestep: "))
N = int(10/dt)
print("dt = {}, N = {}".format(dt,N))
r = np.array([1,0,0])
v = np.array([0,0.5,0])
px = np.zeros(N)
py = np.zeros(N)

for ns in range(N):
	rl = np.sqrt(r.dot(r))
	a = -r/(rl**3)
	r = r + v*dt
	v = v + a*dt
	px[ns] = r[0]
	py[ns] = r[1]

print("Compute ended.")
# animation

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([min(px)-0.2,max(px)+0.2])
ax.set_ylim([min(py)-0.2,max(py)+0.2])
ax.set_aspect('equal')
orbit,  = ax.plot([], [], alpha=0.8, lw=2)
planet, = ax.plot([],[], 'o', color='blue',markersize=2)
sun,    = ax.plot([],[], 'o', color='red',markersize=5)

# initialization function
def init():
    # creating an empty plot/frame
    orbit.set_data([], [])
    planet.set_data([],[])
    sun.set_data([0],[0])
    return orbit,planet,sun

# animation function
def animate(i):
    orbit.set_data(px[:2*i], py[:2*i])
    planet.set_data(px[2*i],py[2*i])
    #ax.set_title('Planet Orbit with t = {:.3f}'.format(t))
    return orbit, planet, sun

def loganim(i,n):
    if (i%100==0): print(f'Saving frame {i} of {n}')
    
# call the animator
anim = animation.FuncAnimation(fig, animate, init_func=init,
							frames=N//2, interval=2, blit=True)

# save the animation as mp4 video file
#anim.save('orbita.mp4', 
#        writer = 'ffmpeg', fps = 30, dpi=100,
#        progress_callback = loganim)

# show the plot
plt.show() 