#!/home/enord/local/miniconda3/envs/ternary/bin/python
import ternary
import matplotlib.pyplot as plt

scale = 100

fig, tax = ternary.figure(scale=scale)

# Boundary and grid
tax.boundary()
tax.gridlines(multiple=10)

# Axis labels
tax.left_axis_label("Z", fontweight='bold')
tax.right_axis_label("Y", fontweight='bold')
tax.bottom_axis_label("X", fontweight='bold')

# Example point
tax.scatter([(30, 50, 20)], marker='o', c='red')

tax.ticks(axis='lbr', multiple=10)
tax.clear_matplotlib_ticks()

plt.show()
