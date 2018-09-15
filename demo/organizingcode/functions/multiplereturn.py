def scale(x, y, z, scale):
    return x * scale, y * scale, z * scale

x, y, z  = scale(10, 20, 30, 1.5)
print(f"{x}, {y}, {z}")
