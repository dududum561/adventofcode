grid = []
instructions = ""
start = (-1, -1)

while True:
  line = input()
  if len(line.strip()) == 0:
    break
  grid.append(list(line))
  if '@' in line:
    start = (len(grid) - 1, line.index('@'))

while True:
  try:
    line = input()
    instructions += line
  except:
    break

dirMap = {
  '>': 0,
  'v': 1,
  '<': 2,
  '^': 3,
}
dr = [0, +1, 0, -1]
dc = [+1, 0, -1, 0]

def isWall(r, c, dir):
  return grid[r + dr[dir]][c + dc[dir]] == '#'

def isEmpty(r, c, dir):
  return grid[r + dr[dir]][c + dc[dir]] == '.'

def moveBoxesLen(r, c, dir):
  r, c = r + dr[dir], c + dc[dir]
  pathLength = 0
  while grid[r][c] == 'O':
    pathLength += 1
    r, c = r + dr[dir], c + dc[dir]
  if grid[r][c] == '#':
    pathLength = 0
  return pathLength

r, c = start
grid[r][c] = '.'

def printGrid():
  grid[r][c] = '@'
  for row in grid:
    print(''.join(row))
  print()
  grid[r][c] = '.'

for dir in instructions:
  dir = dirMap[dir]
  if isWall(r, c, dir): continue
  if isEmpty(r, c, dir):
    r, c = r + dr[dir], c + dc[dir]
    continue
  # it's a box
  length = moveBoxesLen(r, c, dir)
  if length == 0:
    continue
  for i in range(1, length + 2):
    grid[r + dr[dir] * i][c + dc[dir] * i] = 'O'
  r, c = r + dr[dir], c + dc[dir]
  grid[r][c] = '.'

def getCost(r, c):
  return r * 100 + c

ans = 0
for r in range(len(grid)):
  for c in range(len(grid[r])):
    if grid[r][c] == 'O':
      ans += getCost(r, c)
print(ans)