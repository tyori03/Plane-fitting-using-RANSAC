import numpy as np
import random
import sys
import open3d as o3d
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import ransac


pcd = o3d.read_point_cloud("./pc_color_chair.pcd")
o3d.draw_geometries([pcd])

a, b, d = ransac.find_plane(pcd)
print(ransac.angle_rotate(a, b, d))

downpcd = o3d.voxel_down_sample(pcd, voxel_size=0.02)
xyz = np.asarray(downpcd.points)

min_x = np.amin(xyz[:, 0])
max_x = np.amax(xyz[:, 0])
min_y = np.amin(xyz[:, 1])
max_y = np.amax(xyz[:, 1])

x = np.arange(min_x, max_x)
y = np.arange(min_y, max_y)
X,Y = np.meshgrid(x,y)
Z = a*X + b*Y + d

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot_surface(X,Y,Z)
ax.scatter(xyz[:, 0], xyz[:, 1], xyz[:, 2])

plt.show()