import numpy as np

N = 10
cartesian_points = np.random.rand(N, 2) * 100 # Random points in range [0, 100]
print("Cartesian Points:")
print(cartesian_points)

def cartesian_to_polar(points):
    polar_points = np.zeros_like(points)
    for i, (x, y) in enumerate(points):
        r = np.sqrt(x**2 + y**2) #Radius
        theta = np.arctan2(y, x) #Angle in rad
        polar_points[i] = [r, theta]
    return polar_points

polar_points = cartesian_to_polar(cartesian_points)
print("\nPolar Coordinates:")
print(polar_points)