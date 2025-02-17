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
    for i in range(len(dr)):
      rr, cc = r + dr[i], c + dc[i]
      if 0 <= rr and rr < rows and 0 <= cc and cc < cols and grid[rr][cc] == grid[r][c]:
        pass
      else:
        perimeter[id] += 1

ans = 0
for i in range(rows * cols):
  cost = area[i] * perimeter[i]
  ans += cost
print(ans)