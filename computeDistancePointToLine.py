print 'Enter x and y coordinates of the point'
x0 = float(input())
y0 = float(input())

print 'Enter x and y coordinates of point1 then point2 of the line'

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())



def computeDistancePointToLine(x0, y0, x1, y1, x2, y2):
    def computeLineThroughTwoPoints(x1, y1, x2, y2):
        if x1 == x2 and y1 == y2:
            print 'Error, Please give 2 distinct points'
            return(0,0,0)
        else:
            a = (y2 - y1)/((((y2 - y1)**2) + (((x2 - x1)**2)))**(0.5))
            b = (x1 - x2)/((((y2 - y1)**2) + (((x2 - x1)**2)))**(0.5))
            c = (x2*y1 - x1*y2)/((((y2 - y1)**2) + (((x2 - x1)**2)))**(0.5))
            return(a,b,c)
    a, b, c = computeLineThroughTwoPoints(x1, y1, x2, y2)
    return(abs(a*x0 + b*y0 + c))

D = computeDistancePointToLine(x0, y0, x1, y1, x2, y2)
print ("Distance from the point to the line is: %d" %D)
