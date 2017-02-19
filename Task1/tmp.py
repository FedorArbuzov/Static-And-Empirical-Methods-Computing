from math import *
from random import random


# from leather import *

def f(p):
    i = log(1 - p, math.e)
    sq = pow(i, 2.0)
    k = pow(sq, 1/3.0)
    return -1 * k

data = []
for i in range(0, 100):
    r = random()
    if (r == 0): r = random()
    data.append( f(r)  )

print "NOW DATA:"
print ["{:.3f}".format(n) for n in data]


vmin = min(data)
vmax = max(data)

step = (vmax - vmin) / 10.0

score = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for n in data:
    if (n == vmax):
        score[9]+=1
        continue
    dist = n - vmin
    pos = int(dist / step)
    score[pos]+=1

header = []
for i in range(10):
    s =  (vmin + step*i, vmin + step*(i+1))
    header.append(s)

values = []
for n in score:
    s =  n / 100.0
    values.append(s)

header_print = []
for i in range(10):
    s =  "{:.3f},{:.3f}".format(vmin + step*i, vmin + step*(i+1)) 
    header_print.append(s)

values_print = []
for n in score:
    s =  "{:.2f}".format(n / 100.0) 
    values_print.append(s)

print "NOW HEADER:"
print header
print "NOW VALUES:"
print values

import leather

draw = [
    ('Hello', 3),
    ('How', 5),
    ('Are', 9),
    ('You', 4)
]

draw = []
for i in range(10):
    col = (header_print[i], values[i])
    draw.append(col)

chart = leather.Chart('Columns')
chart.add_columns(draw)
chart.to_svg('columns.svg')


