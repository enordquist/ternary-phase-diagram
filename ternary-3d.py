import matplotlib.pyplot as plt
import numpy as np
import argparse


# --- CLI args ---
parser = argparse.ArgumentParser()
parser.add_argument("--gray_axes", nargs="*", choices=["x", "y", "z"], default=[])
parser.add_argument("--colorblind", action="store_true")
parser.add_argument("--nodark", action="store_true")
args = parser.parse_args()

if not args.nodark: plt.style.use('dark_background')

# --- color palettes ---
default_colors = {
  "x": (1, 0, 0),
  "y": (0, 1, 0),
  "z": (0, 0, 1),
}

# colorblind-friendly (Okabe-Ito-ish)
colorblind_colors = {
  "x": (0.9, 0.6, 0.0),   # orange
  "y": (0.0, 0.45, 0.7),  # blue
  "z": (0.0, 0.6, 0.5),   # bluish green
}

colors_axes = colorblind_colors if args.colorblind else default_colors

# override with gray where requested
for ax_name in args.gray_axes:
  colors_axes[ax_name] = (0.3, 0.3, 0.3)

# --- plotting ---
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

n = 50

xdir = np.linspace(0, 1.0, n)
ydir = np.linspace(0, 1.0, n)
zdir = np.linspace(0, 1.0, n)

# Plot direction vectors
ax.plot(xdir, 0, zs=0, zdir='z', c=colors_axes["x"])
ax.plot(0, ydir, zs=0, zdir='z', c=colors_axes["y"])
ax.plot(0, 0, zs=zdir, zdir='z', c=colors_axes["z"])

# Generate simplex points
X, Y = np.meshgrid(xdir, ydir)
Z = 1 - X - Y

mask = Z >= 0
X = X[mask]
Y = Y[mask]
Z = Z[mask]

cx = np.array(colors_axes["x"])
cy = np.array(colors_axes["y"])
cz = np.array(colors_axes["z"])

colors = (X[:, None] * cx +
          Y[:, None] * cy +
          Z[:, None] * cz)
ax.scatter(X, Y, Z, s=40, alpha=0.7, c=colors**0.5)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)

ax.set_xlabel('X', fontweight='bold', color=colors_axes["x"])
ax.set_ylabel('Y', fontweight='bold', color=colors_axes["y"])
ax.set_zlabel('Z', fontweight='bold', color=colors_axes["z"])

ax.tick_params(axis='x', colors=colors_axes["x"])
ax.tick_params(axis='y', colors=colors_axes["y"])
ax.tick_params(axis='z', colors=colors_axes["z"])

ax.xaxis.line.set_color((*colors_axes["x"], 0.0))
ax.yaxis.line.set_color((*colors_axes["y"], 0.0))
ax.zaxis.line.set_color((*colors_axes["z"], 0.0))

ax.view_init(elev=25, azim=45, roll=0)

ax.xaxis._axinfo["grid"]['color'] = (*colors_axes["x"], 0.5)
ax.yaxis._axinfo["grid"]['color'] = (*colors_axes["y"], 0.5)
ax.zaxis._axinfo["grid"]['color'] = (*colors_axes["z"], 0.5)

ax.xaxis._axinfo["grid"]['linewidth'] = 0.5
ax.yaxis._axinfo["grid"]['linewidth'] = 0.5
ax.zaxis._axinfo["grid"]['linewidth'] = 0.5

for t in np.linspace(0, 1, 6):
  ax.plot([t, t],   [0, 1-t], [1-t, 0], color=(*colors_axes["x"], 0.5))
  ax.plot([0, 1-t], [t, t],   [1-t, 0], color=(*colors_axes["y"], 0.5))
  ax.plot([0, 1-t], [1-t, 0], [t, t],   color=(*colors_axes["z"], 0.5))

plt.show()
