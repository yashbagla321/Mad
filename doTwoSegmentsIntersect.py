
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

v1 = [x1, y1]
v2 = [x2, y2]
v3 = [x3, y3]
v4 = [x4, y4]


def doTwoSegmentsIntersect(v1,v2,v3,v4):
    
    num = (x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)
    den = (y4-y3)*(x2-x1) - (x4-x3)*(y2-y1)



    if num == 0 and den == 0:
        return True
    elif num != 0 and den != 0 and x3 != x4:
        s_a = num/den
        s_b = (s_a*(x2-x1) + x1 - x3)/(x4 - x3)
        if s_a >= 0 and s_a <= 1 and s_b >= 0 and s_b <= 1:
            return True
        else:
            return False
            
    else:
        return False
    
    
    
    
print(doTwoSegmentsIntersect(v1,v2,v3,v4))
