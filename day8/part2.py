from collections import deque 

locs = dict()
grid = []
def addLoc(ch, r, c):
  if ch not in locs:
    locs[ch] = []
  locs[ch].append((r, c))

while True:
  try:
    row = input()
    grid.append(row)
    r = len(grid) - 1
    for c in range(len(row)):
      if row[c] != '.':
        addLoc(row[c], r, c)
  except:
    break

valid = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
def addValidLoc(loc, dr, dc):
  r, c = loc
  valid[r][c] = True
  while True:
    r, c = r + dr, c + dc
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]): return
    valid[r][c] = True

for (ch, locations) in locs.items():
  for i in range(len(locations)):
    for j in range(i):
      dr = locations[i][0] - locations[j][0]
      dc = locations[i][1] - locations[j][1]
      addValidLoc(locations[i], dr, dc)
      addValidLoc(locations[j], -dr, -dc)

ans = 0
for row in valid:
  for col in row:
    ans += col
print(ans)