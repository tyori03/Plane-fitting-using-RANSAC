import numpy as np
import math

from sklearn import linear_model

import open3d as o3d

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def find_plane(pcd):
    """
    get coefficient

    Parameters
    ----------
    pcd : open3d.geometry.PointCloud
        PointCloudData

    Returns
    -------
    a, d, d : float
        Coefficients of the plane equation(Z = aX + bY + d).
    """

    xyz = np.asarray(pcd.points)

    # 説明変数
    xy = xyz[:, :2]
    # 目的関数
    z = xyz[:, 2]
    ransac = linear_model.RANSACRegressor(residual_threshold=0.01)

    ransac.fit(xy, z)
    a, b = ransac.estimator_.coef_  # coefficients
    d = ransac.estimator_.intercept_  # intercept

    # print(a, b, d)
    return a, b, d  # Z = aX + bY + d


def angle_rotate(a, b, d):
    """
    get angle of rotation

    Parameters
    ----------
    a, b, d : float
        Coefficients of the plane equation(Z = aX + bY + d).

    Returns
    -------
    rad - math.pi : float
        angle of rotation
    """

    x = np.arange(30)
    y = np.arange(30)
    x, y = np.meshgrid(x, y)
    z = a * x + b * y + d
    rad = math.atan2(y[1][0] - y[0][0], (z[1][0] - z[0][0]))
    return rad - math.pi


def show_graph(x, y, z):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(x, y, z)

    plt.show()


if __name__ == '__main__':
    sample_pcd = o3d.io.read_point_cloud("./pc_color_chair.pcd")
    print(find_plane(sample_pcd))
