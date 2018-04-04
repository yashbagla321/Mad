

x0 = float(input())
y0 = float(input())

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

q = [x0, y0]

v1 = [x1, y1]
v2 = [x2, y2]
v3 = [x3, y3]
v4 = [x4, y4]

P = [v1, v2, v3, v4]

def isPointInConvexPolygon(x, y, poly):

    n = len(poly)
    inside = False

    p1x,p1y = poly[0]
    for i in range(n + 1):
        p2x,p2y = poly[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xints = (y - p1y)*(p2x - p1x)/(p2y - p1y) + p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
        p1x,p1y = p2x,p2y

    return inside


poly = [(0, 10),(10, 10),(10, 0),(0, 0)]

x = 5
y = 5

print(isPointInConvexPolygon(x0, y0, P))