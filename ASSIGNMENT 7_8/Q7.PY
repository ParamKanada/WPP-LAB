# Vectors

import math

class Vector2D:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def rotation_angle(self):
        return math.degrees(math.atan2(self.y, self.x))

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def dotproduct(self, other):
        return self.x * other.x + self.y * other.y

    def crossproduct(self, other):
        return self.x * other.y - self.y * other.x

    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"


class Vector3D(Vector2D):
    
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    def dotproduct(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def crossproduct(self, other):
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def __str__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"
    
b = int(input("\nEnter X coordinate for vector 1 = \n"))
c = int(input("Enter Y coordinate for vector 1 = \n"))
v1 = Vector2D(b,c)

d = int(input("\nEnter X coordinate for vector 2 = \n"))
e = int(input("Enter Y coordinate for vector 2 = \n"))
v2 = Vector2D(d,e)

print("\nFor 1and 2 \n")
print(f"Magnitude: {v1.magnitude()}")
print(f"Rotation Angle: {v1.rotation_angle()}°")
print(f"Distance to v2: {v1.distance(v2)}")
print(f"Dot Product: {v1.dotproduct(v2)}")
print(f"Cross Product: {v1.crossproduct(v2)}")

f = int(input("\nEnter X coordinate for vector 3 = \n"))
g = int(input("Enter Y coordinate for vector 3 = \n"))
h = int(input("Enter Z coordinate for vector 3 = \n"))
v3 = Vector3D(f,g,h)

i = int(input("\nEnter X coordinate for vector 4 = \n"))
j = int(input("Enter Y coordinate for vector 4 = \n"))
k = int(input("Enter Z coordinate for vector 4 = \n"))
v4 = Vector3D(i,j,k)

print("\nFor 3 and 4 \n")
print(f"Magnitude: {v3.magnitude()}")
print(f"Distance to v4: {v3.distance(v4)}")
print(f"Dot Product: {v3.dotproduct(v4)}")
print(f"Cross Product: {v3.crossproduct(v4)}")