import sys

positions = []
velocities = []

def parseCoord(s):
  s = s[2:].split(",")
  x, y = (int(x) for x in s)
  return x, y

while True:
  try:
    pstr, vstr = input().strip().split(" ")
    positions.append(parseCoord(pstr))
    velocities.append(parseCoord(vstr))
  except:
    break

X, Y = 101, 103

def sanitize(pos, dx, dy):
  x, y = pos
  x += dx
  y += dy
  x = (x % X + X) % X
  y = (y % Y + Y) % Y
  return x, y

for ITERS in range(100000):
  grid = [['.' for _ in range(X)] for _ in range(Y)]
  for i in range(len(positions)):
    pos = positions[i]
    vel = velocities[i]
    dx = vel[0] * ITERS
    dy = vel[1] * ITERS
    x, y = sanitize(pos, dx, dy)
    grid[y][x] = '*'

  def checkTree():
    for row in grid:
      if "**************" in ''.join(row):
        return True
    return False

  if checkTree():
    print("FOUND: ", ITERS, file=sys.stderr)
    print(ITERS)
    for row in grid:
      print(''.join(row))