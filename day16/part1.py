from queue import PriorityQueue

grid = []
start, end = (-1, -1), (-1, -1)

while True:
  try:
    line = input().strip()
    grid.append(list(line))
    if 'S' in line:
      start = (len(grid) - 1, line.index('S'))
    if 'E' in line:
      end = (len(grid) - 1, line.index('E'))
  except:
    break

oo = 1000000000000
rows, cols = len(grid), len(grid[0])

sr, sc = start
er, ec = end

dr = [0, -1, 0, +1]
dc = [+1, 0, -1, 0]

queue = PriorityQueue()
dist = [[[oo for _ in range(cols)] for _ in range(rows)] for _ in range(len(dr))]

queue.put((0, 0, sr, sc))
dist[0][sr][sc] = 0

while not queue.empty():
  d, dir, r, c = queue.get()
  if d > dist[dir][r][c]: continue
  # try rotating
  for dirDelta in [-1, +1]:
    ndir = (dir + dirDelta + len(dr)) % len(dr)
    nd = d + 1000
    if dist[ndir][r][c] > nd:
      dist[ndir][r][c] = nd
      queue.put((nd, ndir, r, c))
  # try moving
  rr, cc = r + dr[dir], c + dc[dir]
  if grid[rr][cc] != '#' and dist[dir][rr][cc] > d + 1:
    dist[dir][rr][cc] = d + 1
    queue.put((d + 1, dir, rr, cc))

ans = oo
for dir in range(4):
  ans = min(ans, dist[dir][er][ec])
print(ans)