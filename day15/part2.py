from collections import deque

grid = []
instructions = ""
start = (-1, -1)

while True:
  line = input()
  if len(line.strip()) == 0:
    break
  row = ""
  for ch in line:
    if ch == '#': row += '##'
    if ch == 'O': row += '[]'
    if ch == '.': row += '..'
    if ch == '@': row += '@.'
  grid.append(list(row))
  if '@' in row:
    start = (len(grid) - 1, row.index('@'))

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

def isBox(r, c, dir):
  ch = grid[r + dr[dir]][c + dc[dir]]
  return ch == '[' or ch == ']'

def isEmpty(r, c, dir):
  return grid[r + dr[dir]][c + dc[dir]] == '.'

def isWall(r, c, dir=-1):
  if dir == -1: return grid[r][c] == '#'
  return grid[r + dr[dir]][c + dc[dir]] == '#'

r, c = start
grid[r][c] = '.'

def printGrid():
  grid[r][c] = '@'
  for row in grid:
    print(''.join(row))
  print()
  grid[r][c] = '.'

def getTouchingBoxes(r, c, dir):
  queue = deque([(r, c)])
  if grid[r][c] == '[': queue.append((r, c + 1))
  if grid[r][c] == ']': queue.append((r, c - 1))

  ret = []
  done = set()
  while len(queue) > 0:
    r, c = queue.popleft()
    if grid[r][c] == '[': ret.append((r, c))
    if isBox(r, c, dir) and (r + dr[dir], c + dc[dir]) not in done:
      queue.append((r + dr[dir], c + dc[dir]))
      done.add((r + dr[dir], c + dc[dir]))
    if grid[r][c] == '[' and (r, c + 1) not in done:
      queue.append((r, c + 1))
      done.add((r, c + 1))
    if grid[r][c] == ']' and (r, c - 1) not in done:
      queue.append((r, c - 1))
      done.add((r, c - 1))
  return ret

def moveBoxes(sr, sc, dir):
  # get all cells with boxes touching (left sides)
  cells = getTouchingBoxes(sr + dr[dir], sc + dc[dir], dir)
  # check if boxes can be moved
  for (r, c) in cells:
    if isWall(r + dr[dir], c + dc[dir]) or isWall(r + dr[dir], c + dc[dir] + 1):
      return sr, sc # can't move boxes
  # zero out existing cells
  for (r, c) in cells:
    grid[r][c] = grid[r][c + 1] = '.'
  # move boxes to new cells
  for (r, c) in cells:
    grid[r + dr[dir]][c + dc[dir]] = '['
    grid[r + dr[dir]][c + dc[dir] + 1] = ']'
  return sr + dr[dir], sc + dc[dir]

for dir in instructions:
  dir = dirMap[dir]
  if isWall(r, c, dir): continue
  if isEmpty(r, c, dir):
    r, c = r + dr[dir], c + dc[dir]
    continue
  # it's a box
  r, c = moveBoxes(r, c, dir)

def getCost(r, c):
  return r * 100 + c

ans = 0
for r in range(len(grid)):
  for c in range(len(grid[r])):
    if grid[r][c] == '[':
      ans += getCost(r, c)
print(ans)