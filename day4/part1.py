grid = []
while True:
  try:
    row = input()
    grid.append(row)
  except:
    break

XMAS = "XMAS"
ans = 0

for dr in range(-1, +2):
  for dc in range(-1, +2):
    if dr == 0 and dc == 0: continue
    for r in range(len(grid)):
      for c in range(len(grid[r])):
        valid = True
        for length in range(len(XMAS)):
          rr = r + dr * length
          cc = c + dc * length
          if rr < 0 or cc < 0 or rr >= len(grid) or cc >= len(grid[r]):
            valid = False
            break
          valid = valid and grid[rr][cc] == XMAS[length]
        ans += valid

print(ans)