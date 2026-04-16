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

ax.set_xlabel('X', fontweight='bold')
ax.set_ylabel('Y', fontweight='bold')
ax.set_zlabel('Z', fontweight='bold')

ax.view_init(elev=25, azim=45, roll=0)

plt.show()
