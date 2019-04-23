cameras = [[60, 1], [160, 2], [170, 5], [220, 6], [290,7]]
limit_speed = 60

spot = 0
time = 0
result = 0

for camera in cameras:
    if (camera[0] - spot) // (camera[1] - time) > limit_speed:
        result += 1
    spot = camera[0]
    time = camera[1]

print(result)
