grid = []
loc = (-1, -1)
while True:
  try:
    row = list(input())
    grid.append(row)
    if '^' in row:
      loc = (len(grid) - 1, row.index('^'))
  except:
    break

dr = [-1, 0, +1,  0]
dc = [0, +1,  0, -1]

visited = [[[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))] for _ in range(len(dr))]

def hasLoop(id):
  def inRange(r, c):
    return r >= 0 and c >= 0 and r < len(grid) and c < len(grid[r])
  def isValid(r, c):
    return grid[r][c] != '#'
  
  r, c = loc
  dir = 0
  visited[dir][r][c] = id

  while True:
    rr, cc = r + dr[dir], c + dc[dir]
    if not inRange(rr, cc):
      return False
    if not isValid(rr, cc):
      dir = (dir + 1) % len(dr)
      if visited[dir][r][c] == id: return True
      visited[dir][r][c] = id
    else:
      r, c = rr, cc
      if visited[dir][r][c] == id: return True
      visited[dir][r][c] = id

ans = 0
for r in range(len(grid)):
  for c in range(len(grid[0])):
    if grid[r][c] != '.': continue
    grid[r][c] = '#'
    ans += hasLoop(r * 1000000 + c)
    grid[r][c] = '.'
print(ans)