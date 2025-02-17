grid = []

class DSU:
  def __init__(self, size):
    self.parent = list(range(size))
  def findId(self, v):
    if v == self.parent[v]:
      return v
    self.parent[v] = self.findId(self.parent[v])
    return self.parent[v]
  def union(self, u, v):
    u, v = self.findId(u), self.findId(v)
    if u != v:
      self.parent[u] = v

while True:
  try:
    row = input()
    grid.append(row)
  except:
    break

rows, cols = len(grid), len(grid[0])
dr = [0, -1, 0, +1]
dc = [+1, 0, -1, 0]

dsu = DSU(rows * cols)
def getId(r, c):
  return r * cols + c

for r in range(rows):
  for c in range(cols):
    for i in range(len(dr)):
      rr, cc = r + dr[i], c + dc[i]
      if 0 <= rr and rr < rows and 0 <= cc and cc < cols and grid[rr][cc] == grid[r][c]:
        dsu.union(getId(r, c), getId(rr, cc))

area = [0] * (rows * cols)
perimeter = [0] * (rows * cols)

for r in range(rows):
  for c in range(cols):
    id = dsu.findId(getId(r, c))
    area[id] += 1
    neighbors = [False] * 4
    for i in range(len(dr)):
      rr, cc = r + dr[i], c + dc[i]
      if 0 <= rr and rr < rows and 0 <= cc and cc < cols and grid[rr][cc] == grid[r][c]:
        neighbors[i] = True
    # find convex corners
    for i in range(4):
      if neighbors[i]: continue
      for j in range(i):
        if i == (j ^ 2):
          continue
        if not neighbors[j]:
          perimeter[id] += 1
    # find concave corners
    for i in range(4):
      j = (i + 1) % 4
      if not neighbors[i] or not neighbors[j]: continue
      rr, cc = r + dr[i] + dr[j], c + dc[i] + dc[j]
      if grid[rr][cc] != grid[r][c]:
        perimeter[id] += 1

ans = 0
for i in range(rows * cols):
  cost = area[i] * perimeter[i]
  ans += cost
print(ans)