from collections import deque

isSmallCase = False

if isSmallCase:
  n = 7
else:
  n = 71


coords = []
while True:
  try:
    r, c = (int(x) for x in input().strip().split(","))
    coords.append((r, c))
  except:
    break

dr = [-1, 0, +1, 0]
dc = [0, +1, 0, -1]

def bfs(toFall):
  grid = [['.' for _ in range(n)] for _ in range(n)]
  for i in range(toFall):
    r, c = coords[i]
    grid[r][c] = '#'

  dist = [[-1 for _ in range(n)] for _ in range(n)]

  queue = deque([(0, 0)])
  dist[0][0] = 0

  while len(queue) > 0:
    r, c = queue.popleft()
    for i in range(len(dr)):
      rr, cc = r + dr[i], c + dc[i]
      if rr < 0 or cc < 0 or rr >= n or cc >= n: continue
      if grid[rr][cc] == '#': continue
      if dist[rr][cc] != -1: continue
      dist[rr][cc] = dist[r][c] + 1
      queue.append((rr, cc))

  return dist[n - 1][n - 1]

low = 0
high = len(coords)
while low <= high:
  mid = (low + high) // 2
  if bfs(mid) == -1:
    high = mid - 1
  else:
    low = mid + 1

print(coords[high])