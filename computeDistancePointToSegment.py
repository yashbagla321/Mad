print 'Enter x and y coordinates of the point'
x0 = float(input())
y0 = float(input())

print 'Enter x and y coordinates of point1 then point2 of the line'

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())



import math

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

    # Note: If the actual distance does not matter,
    # if you only want to compare what this function
    # returns to other results of this function, you
    # can just return the squared distance instead
    # (i.e. remove the sqrt) to gain a little performance

    dist = math.sqrt(dx*dx + dy*dy)

    return dist

print(computeDistancePointToSegment(x1, y1, x2, y2, x0, y0))