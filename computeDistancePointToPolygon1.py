from shapely import wkt
poly = wkt.loads('POLYGON((30 10, 40 40, 20 40, 10 20, 30 10))')
pt = wkt.loads('POINT(20 20)')

poly.distance(pt)  # 0.0

poly.boundary.distance(pt)  # 4.47213595499958

poly.exterior.distance(pt)  # 4.47213595499958