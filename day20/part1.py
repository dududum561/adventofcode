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

def bfs(init, grid, initDist=0):
  queue = deque([(init[0], init[1])])
  dist = [[oo for _ in range(cols)] for _ in range(rows)]
  dist[init[0]][init[1]] = initDist
  while len(queue) > 0:
    r, c = queue.popleft()
    for i in range(len(dr)):
      rr, cc = r + dr[i], c + dc[i]
      if outOfRange(rr, cc) or grid[rr][cc] == '#' or dist[rr][cc] != oo: continue
      dist[rr][cc] = dist[r][c] + 1
      queue.append((rr, cc))
  return dist

forward, backward = bfs(start, grid), bfs(end, grid, 1)
originalDist = forward[end[0]][end[1]]

THRESHOLD = 100
ans = set()

for r in range(rows):
  for c in range(cols):
    for i in range(len(dr)):
      for j in range(len(dr)):
        rPrev, cPrev = r + dr[i], c + dc[i]
        rNext, cNext = r + dr[j], c + dc[j]
        if outOfRange(rPrev, cPrev) or outOfRange(rNext, cNext): continue
        d = forward[rPrev][cPrev] + 1 + backward[rNext][cNext]
        savedDist = originalDist - d
        if savedDist >= THRESHOLD:
          ans.add(((rPrev, cPrev), (rNext, cNext)))

print(len(ans))