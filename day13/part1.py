def parseButton(line: str):
  line = line[len("Button A: ")-1:].strip()
  x, y = line.split(", ")
  return int(x[2:]), int(y[2:])

def parsePrize(line):
  line = line[len("Prize: ")-1:].strip()
  x, y = line.split(", ")
  return int(x[2:]), int(y[2:])

def solve(a, b, prize):
  ax, ay = a
  bx, by = b
  px, py = prize
  ans = 0
  for aTries in range(101):
    x = ax * aTries
    y = ay * aTries
    xRem = px - x
    yRem = py - y
    if xRem < 0 or yRem < 0: continue
    if xRem % bx != 0 or yRem % by != 0: continue
    if xRem // bx != yRem // by: continue
    bTries = xRem // bx
    cost = aTries * 3 + bTries * 1
    if ans == 0 or cost < ans:
      ans = cost
  return ans

ans = 0
while True:
  try:
    a = parseButton(input())
    b = parseButton(input())
    prize = parsePrize(input())
    ans += solve(a, b, prize)
    input()
  except:
    break

print(ans)