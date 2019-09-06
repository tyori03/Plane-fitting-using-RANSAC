# Plane-fitting-with-RANSAC
Plane fitting with RANSAC written in Python.

Python上でRANSAC法を用いて平面推定を行うプログラム

https://user-images.githubusercontent.com/48345625/64425417-9d340b80-d0e6-11e9-8326-c430668e06b3.png

https://user-images.githubusercontent.com/48345625/64425465-b472f900-d0e6-11e9-9d7e-1461562c5df6.png

## Description
This program finds the equation of a plane from Point Cloud by using RANSAC.

* input: Point Cloud data(.pcd)
* output: a, b, d (coefficient: Z = a*X + b*Y + d), Angle of rotation(radian)

## Requirement
import open3d, sklearn, matplot

## Usage
1. Put ransac.py on your project 
2. import ransac
3. find_plane(pcd): You can get confficient. angle_rotate(a, b, d): You can get angle of rotation(radian for leveling)

Sorry, if my English is incorrect :(
