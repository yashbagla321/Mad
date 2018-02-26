import math


print 'Enter x and y coordinates of the point'
x0 = float(input())
y0 = float(input())

print 'Enter the no of vertices'
n = int(input())

X = []
Y = []
D = []
print 'Enter x coordinates of all the vertices in order'
for i in range(n):
    X.append(float(input()))

print 'Enter y coordinates of all the vertices in order'
for i in range(n):
    Y.append(float(input()))


def computeDistancePointToPolygon(x0, y0, X, Y):
    def point_inside_polygon(x, y, X, Y):

        n = len(X)
        inside = False

        p1x = X[0]
        p1y = Y[0]
        for i in range(n+1):
            p2x = X[i % n]
            p2y = Y[i % n]
            if y > min(p1y,p2y):
                if y <= max(p1y,p2y):
                    if x <= max(p1x,p2x):
                        if p1y != p2y:
                            xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x,p1y = p2x,p2y
    
        return inside

    check = point_inside_polygon(x0, y0, X, Y)
    if check != False:
        print 'The point is inside the polygon'
        return 0
    else:
        def computeDistancePointToSegment(x1,y1, x2,y2, x3,y3): # x3,y3 is the point
            px = x2-x1
            py = y2-y1

            something = px*px + py*py

            u =  ((x3 - x1) * px + (y3 - y1) * py) / float(something)

            if u > 1:
                u = 1
            elif u < 0:
                u = 0

            x = x1 + u * px
            y = y1 + u * py

            dx = x - x3
            dy = y - y3

            dist = math.sqrt(dx*dx + dy*dy)

            return dist

        for i in range(n):
            D.append(computeDistancePointToSegment(X[i%n], Y[i%n], X[(i+1)%n], Y[(i+1)%n], x0 ,y0))

        D_min = D[0]
        i_min = 0
        for i in range(n):
            if D[i] < D_min:
                D_min = D[i]
                i_min = i
        return (D_min, i_min)    

D_min, i_min = computeDistancePointToPolygon(x0, y0, X, Y)

m = -(x0 - X[i_min])/(y0 - Y[i_min])

ux = -m/(1 + (m)**2)**0.5
uy = 1/(1 + (m)**2)**0.5

u = [ux,
     uy]
print u

