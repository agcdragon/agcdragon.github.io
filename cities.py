
from math import pi , acos , sin , cos

d = {}
loc = {}
def main():
  with open('rrNodes.txt') as f:
    for line in f:
      n = line.split()
      d[n[0]] = (n[1], n[2], list()) # third value is a list of neighbors
  with open('rrEdges.txt') as f:
    for line in f:
      n = line.split()
      d[n[0]][2].append(n[1])
      d[n[1]][2].append(n[0])
  with open('rrNodeCity.txt') as f:
    for line in f:
      id = line[0:7]
      name = line[8:]
      name = name.strip()
      loc[name] = id

def heuristic(a, b):
  if a==b:
    return 0
  start = d[a]
  dest = d[b]

  y1, x1 = start[0], start[1]
  y2, x2 = dest[0], dest[2]
  
  return calcd(y1, x1, y2, x2)

def calcd(y1,x1, y2,x2):
   #
   # y1 = lat1, x1 = long1
   # y2 = lat2, x2 = long2
   # all assumed to be in decimal degrees

   # if (and only if) the input is strings
   # use the following conversions

   y1  = float(y1)
   x1  = float(x1)
   y2  = float(y2)
   x2  = float(x2)
   #
   R   = 3958.76 # miles = 6371 km
   #
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0
   #
   # approximate great circle distance with law of cosines
   #
   return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R



