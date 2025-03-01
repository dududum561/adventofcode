from collections import deque

grid = []
start = (-1, -1)
end = (-1, -1)

while True:
  try:
    row = list(input().strip())
    grid.append(row)
    if 'S' in row:
      start = (len(grid) - 1, row.index('S'))
    if 'E' in row:
      end =   (len(grid) - 1, row.index('E'))
  except:
    break

rows, cols = len(grid), len(grid[0])
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
oo = 10 ** 25

def outOfRange(r, c):
  return r < 0 or c < 0 or r >= rows or c >= cols

def bfs(init, grid):
  queue = deque([(init[0], init[1])])
  dist = [[oo for _ in range(cols)] for _ in range(rows)]
  dist[init[0]][init[1]] = 0
  while len(queue) > 0:
    r, c = queue.popleft()
    for i in range(len(dr)):
      rr, cc = r + dr[i], c + dc[i]
      if outOfRange(rr, cc) or grid[rr][cc] == '#' or dist[rr][cc] != oo: continue
      dist[rr][cc] = dist[r][c] + 1
      queue.append((rr, cc))
  return dist

forward, backward = bfs(start, grid), bfs(end, grid)
originalDist = forward[end[0]][end[1]]

THRESHOLD = 100
MAX_CHEATS = 20

ans = set()

for i in range(-MAX_CHEATS, +MAX_CHEATS + 1):
  for j in range(-MAX_CHEATS, +MAX_CHEATS + 1):
    if abs(i) + abs(j) > MAX_CHEATS: continue
    for r in range(rows):
      for c in range(cols):
        rr, cc = r + i, c + j
        if outOfRange(rr, cc): continue
        d = forward[r][c] + abs(i) + abs(j) + backward[rr][cc]
        savedDist = originalDist - d
        if savedDist >= THRESHOLD:
          ans.add(((r, c), (rr, cc)))

print(len(ans))