import math 
def structure(p, q, r): 
    v = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1]) 
    if v == 0: 
        return 0 
    return 1 if v > 0 else 2  

def gs(points): 
    n = len(points) 
    if n < 3: 
        return [] 
    min_pt = min(points, key=lambda x: (x[1], x[0])) 
    print(min_pt)
    sort_pts = sorted(points, key=lambda x: (math.atan2(x[1] - min_pt[1], x[0] - min_pt[0]), x)) 
    print(sort_pts)
    stack = [sort_pts[0], sort_pts[1], sort_pts[2]] 
    print(f"After addition 3 points , stack : {stack}") 
    for i in range(3, n): 
        while len(stack) > 1 and structure(stack[-2], stack[-1], sort_pts[i]) != 2: 
            stack.pop() 
        stack.append(sort_pts[i]) 
        print(f"adding {sort_pts[i]} --> stack : {stack}") 
    return stack 
points =[(0, 0), (3, 1), (1, 4), (3, 3), (5, 2), (5, 5), (9, 6), (7, 0)]
print(f"Convex hull will be : {gs(points)}") 