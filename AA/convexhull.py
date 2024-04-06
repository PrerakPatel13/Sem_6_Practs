import math

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - \
          (q[0] - p[0]) * (r[1] - q[1])
  
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def graham_scan(points):
    n = len(points)
    if n < 3:
        return None
  
    min_point = min(points, key=lambda x: (x[1], x[0]))
    min_index = points.index(min_point)

    points[0], points[min_index] = points[min_index], points[0]

    def polar_angle(p):
        return math.atan2(p[1] - points[0][1], p[0] - points[0][0])

    points[1:] = sorted(points[1:], key=polar_angle)

    stack = [points[0], points[1], points[2]]

    for i in range(3, n):
        while len(stack) > 1 and orientation(stack[-2], stack[-1], points[i]) != 2:
            stack.pop()
        stack.append(points[i])

    return stack

points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
convex_hull = graham_scan(points)
print("Convex Hull Points:")
for point in convex_hull:
    print(point)
