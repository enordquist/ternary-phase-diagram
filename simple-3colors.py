import ternary
import math
import matplotlib.pyplot as plt

# colorblind (IBM)
colorblind_colors = {
  "x": (220/255,  38/255, 127/255),   # magenta
  "y": (225/255, 176/255, 0),         # yellow
  "z": (100/255, 143/255, 255/255),   # blue
}

def color_point(x, y, z, scale):
  fx, fy, fz = x/scale, y/scale, z/scale

  r = fx * colorblind_colors["x"][0] + fy * colorblind_colors["y"][0] + fz * colorblind_colors["z"][0]
  g = fx * colorblind_colors["x"][1] + fy * colorblind_colors["y"][1] + fz * colorblind_colors["z"][1]
  b = fx * colorblind_colors["x"][2] + fy * colorblind_colors["y"][2] + fz * colorblind_colors["z"][2]

  return (r, g, b, 1.0)

def generate_heatmap_data(scale=5):
    from ternary.helpers import simplex_iterator
    d = dict()
    for (i, j, k) in simplex_iterator(scale):
        d[(i, j, k)] = color_point(i, j, k, scale)
    return d

scale = 90
data = generate_heatmap_data(scale)
figure, tax = ternary.figure(scale=scale)
tax.heatmap(data, style="hexagonal", use_rgba=True, colorbar=False)
# Remove default Matplotlib Axes
tax.clear_matplotlib_ticks()
tax.get_axes().axis('off')
tax.boundary()
plt.show()
