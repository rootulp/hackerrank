import sys
import math

# tan(angle_bca) = sides[0] / sides[1]
# angle of MBC = 180 - 90 - angle_bca
sides = []
for line in sys.stdin:
    sides.append(int(line.rstrip()))
opposite = sides[0]
adjacent = sides[1]
angle_mbc = int(round(math.degrees(math.atan2(opposite,adjacent))))

degree_sign= u'\N{DEGREE SIGN}'
print(str(angle_mbc) + degree_sign)

