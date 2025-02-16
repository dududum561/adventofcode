grid = []
while True:
  try:
    row = input()
    grid.append(row)
  except:
    break

ans = 0

for r in range(1, len(grid) - 1):
  for c in range(1, len(grid[r]) - 1):
    if grid[r][c] != 'A': continue
    diag1 = ''.join(sorted([grid[r - 1][c - 1], grid[r + 1][c + 1]]))
    diag2 = ''.join(sorted([grid[r - 1][c + 1], grid[r + 1][c - 1]]))
    if diag1 != diag2: continue
    if diag1 != "MS": continue
    ans += 1

print(ans)