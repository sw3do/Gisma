from threeD import cube, sphere
import circle

# Circle
r = 5
print("Circle circumference:", circle.circumference(r))

# Cube
s = 3
print("Cube surface area:", cube.surface_area(s))
print("Cube volume:", cube.volume(s))
print("Cube perimeter:", cube.perimeter(s))

# Sphere
r2 = 4
print("Sphere surface area:", sphere.surface_area(r2))
print("Sphere volume:", sphere.volume(r2))
