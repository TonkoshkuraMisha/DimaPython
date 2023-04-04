x_coord = list(map(int, input().split()))
y_coord = list(map(int, input().split()))
T_point = tuple(map(int, input().split()))
points = enumerate(zip(x_coord, y_coord), start = 1)
distance = 0
max_x = 0
max_y = 0
index = 0
for i, (x, y) in points:
    if pow((pow((x-T_point[0]), 2) + pow((y-T_point[1]), 2)), 0.5) >= distance:
        distance = pow((pow((x-T_point[0]), 2) + pow((y-T_point[1]), 2)), 0.5)
        max_x = x
        max_y = y
        index = i
print(index)

