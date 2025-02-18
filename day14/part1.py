ITERS = 100

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

newPositions = []
for i in range(len(positions)):
  pos = positions[i]
  vel = velocities[i]
  dx = vel[0] * ITERS
  dy = vel[1] * ITERS
  x, y = sanitize(pos, dx, dy)
  newPositions.append((x, y))

quadrants = [0] * 4
for (x, y) in newPositions:
  if x == X // 2 or y == Y // 2: continue
  x = x > X // 2
  y = y > Y // 2
  quadrants[x * 2 + y] += 1

ans = 1
for x in quadrants:
  ans *= x
print(ans)
