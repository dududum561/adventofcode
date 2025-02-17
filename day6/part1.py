grid = []
loc = (-1, -1)
while True:
  try:
    row = input()
    grid.append(row)
    idx = row.find('^')
    if idx != -1:
      loc = (len(grid) - 1, idx)
  except:
    break

visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

r, c = loc
visited[r][c] = True

dr = [-1, 0, +1,  0]
dc = [0, +1,  0, -1]

def inRange(r, c):
  return r >= 0 and c >= 0 and r < len(grid) and c < len(grid[r])
def isValid(r, c):
  return grid[r][c] != '#'

dir = 0
while True:
  rr, cc = r + dr[dir], c + dc[dir]
  if not inRange(rr, cc):
    break
  if not isValid(rr, cc):
    dir = (dir + 1) % len(dr)
  else:
    r, c = rr, cc
    visited[r][c] = True

ans = 0
for row in visited:
  for col in row:
    ans += col
print(ans)