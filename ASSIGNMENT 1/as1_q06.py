'''6. Consider a 3-D co-ordinate space. Input 10 3-D points. Find the nearest neighbour for each
of the points in your 3-D space and store them in a list. The final output is a list with each
consisting of a point and its nearest neighbour. [Hint: Use distance between two points
formula]'''

#idea: i will make a list of tupples
import math

def find_distance(point1, point2):
    a, b, c = point1
    x, y, z = point2
    return math.sqrt((a - x) ** 2 + (b - y) ** 2 + (c - z) ** 2)

coordinates_ls = []
for i in range(3):
    x = float(input(f"Enter the x coordinate of point {i}: "))
    y = float(input(f"Enter the y coordinate of point {i}: "))
    z = float(input(f"Enter the z coordinate of point {i}: "))    
    coordinates_ls.append((x,y,z))

nearest_ls=[]
for point in coordinates_ls:
    min_dist = 9999999999999    #lets just say
    for other_point in coordinates_ls:
        if point != other_point:
            dist = find_distance(point,other_point)
            if dist<min_dist:
                min_dist=dist
                nearest_point = other_point
    nearest_ls.append((point,nearest_point))


print("Point and its Nearest Neighbor:")
for pair in nearest_ls:
    print(f"Point: {pair[0]}, Nearest Neighbor: {pair[1]}")