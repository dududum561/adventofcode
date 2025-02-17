from collections import deque

grid = []
while True:
  try:
    row = [int(x) for x in list(input())]
    grid.append(row)
  except:
    break

rows, cols = len(grid), len(grid[0])
def getId(r, c):
  return r * cols + c

ways = [[0 for _ in range(cols)] for _ in range(rows)]
queue = deque()
visited = [[False for _ in range(cols)] for _ in range(rows)]

for r in range(rows):
  for c in range(cols):
    if grid[r][c] == 9:
      ways[r][c] = 1
      queue.append((r, c))
      visited[r][c] = True

dr = [0, -1,  0, +1]
dc = [+1, 0, -1,  0]

while len(queue) > 0:
  r, c = queue.popleft()
  for i in range(len(dr)):
    rr, cc = r + dr[i], c + dc[i]
    if rr < 0 or cc < 0 or rr >= rows or cc >= cols: continue
    if grid[rr][cc] != grid[r][c] - 1: continue
    ways[rr][cc] += ways[r][c]
    if visited[rr][cc]: continue
    visited[rr][cc] = True
    queue.append((rr, cc))

ans = 0
for r in range(rows):
  for c in range(cols):
    if grid[r][c] == 0:
      ans += ways[r][c]
print(ans)