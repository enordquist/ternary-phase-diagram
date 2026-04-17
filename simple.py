import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

n = 50

xdir = np.linspace(0, 1.0, n)
ydir = np.linspace(0, 1.0, n)
zdir = np.linspace(0, 1.0, n)

# Plot direction vectors
ax.plot(xdir, 0, zs=0, zdir='z',c=(1,0,0))
ax.plot(0, ydir, zs=0, zdir='z',c=(0,1,0))
ax.plot(0, 0, zs=zdir, zdir='z',c=(0,0,1))

# Generate simplex points
X, Y = np.meshgrid(xdir, ydir)
Z = 1 - X - Y

mask = Z >= 0  # keep only valid simplex points
X = X[mask]
Y = Y[mask]
Z = Z[mask]

colors = np.vstack((X, Y, Z)).T
ax.scatter(X, Y, Z, s=10, alpha=0.5, c=colors**0.5)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)

ax.set_xlabel('X', fontweight='bold', color=(1,0,0))
ax.set_ylabel('Y', fontweight='bold', color=(0,1,0))
ax.set_zlabel('Z', fontweight='bold', color=(0,0,1))

ax.tick_params(axis='x', colors=(1,0,0))
ax.tick_params(axis='y', colors=(0,1,0))
ax.tick_params(axis='z', colors=(0,0,1))

ax.xaxis.line.set_color((1,0,0,0.0))
ax.yaxis.line.set_color((0,1,0,0.0))
ax.zaxis.line.set_color((0,0,1,0.0))

ax.view_init(elev=25, azim=45, roll=0)

ax.xaxis._axinfo["grid"]['color'] = (1, 0, 0, 0.5)
ax.yaxis._axinfo["grid"]['color'] = (0, 1, 0, 0.5)
ax.zaxis._axinfo["grid"]['color'] = (0, 0, 1, 0.5)

ax.xaxis._axinfo["grid"]['linewidth'] = 0.5
ax.yaxis._axinfo["grid"]['linewidth'] = 0.5
ax.zaxis._axinfo["grid"]['linewidth'] = 0.5

for t in np.linspace(0, 1, 6):
  ax.plot([t, t],   [0, 1-t], [1-t, 0], color=(1,0,0,0.5))
  ax.plot([0, 1-t], [t, t],   [1-t, 0], color=(0,1,0,0.5))
  ax.plot([0, 1-t], [1-t, 0], [t, t],   color=(0,0,1,0.5))

plt.show()
