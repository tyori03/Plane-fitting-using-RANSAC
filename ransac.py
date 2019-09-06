import numpy as np
import math

from sklearn import linear_model

import open3d as o3d

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def find_plane(pcd):
    xyz = np.asarray(pcd.points)

    # 説明変数
    XY = xyz[:, :2]
    # 目的関数
    Z = xyz[:, 2]
    ransac = linear_model.RANSACRegressor(residual_threshold=0.01)

    ransac.fit(XY, Z)
    a, b = ransac.estimator_.coef_  # 係数
    d = ransac.estimator_.intercept_  # 切片

    print(a, b, d)
    return a, b, d  # Z = aX + bY + d


def angle_rotate(a, b, d):
    x = np.arange(30)
    y = np.arange(30)
    X, Y = np.meshgrid(x, y)
    Z = a * X + b * Y + d
    rad = math.atan2(Y[1][0] - Y[0][0], (Z[1][0] - Z[0][0]))
    return rad - math.pi


def show_graph(X, Y, Z):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(X, Y, Z)

    plt.show()


if __name__ == '__main__':

    pcd = o3d.read_point_cloud("./data/pc_color_chair.pcd")
    find_plane(pcd)