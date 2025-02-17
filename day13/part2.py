OFFSET = 10000000000000

def parseButton(line: str):
  line = line[len("Button A: ")-1:].strip()
  x, y = line.split(", ")
  return int(x[2:]), int(y[2:])

def parsePrize(line):
  line = line[len("Prize: ")-1:].strip()
  x, y = line.split(", ")
  return int(x[2:]) + OFFSET, int(y[2:]) + OFFSET

'''
a * a_x + b * b_x = X
a * a_y + b * b_y = Y

a = (X - b * b_x) / a_x
a = (Y - b * b_y) / a_y

X / a_x - b * b_x / a_x = Y / a_y - b * b_y / a_y
-b * b_x / a_x + b * b_y / a_y = Y / a_y - X / a_x
b * (-b_x / a_x + b_y / a_y) = Y / a_y - X / a_x
b = (Y / a_y - X / a_x) / (b_y / a_y - b_x / a_x)

minimize(x * 3 + y)
'''

def solve(A, B, prize):
  ax, ay = A
  bx, by = B
  X, Y = prize
  
  b = (Y / ay - X / ax) / (by / ay - bx / ax)
  b = int(round(b))

  a = (X - b * bx) / ax
  a = int(round(a))

  if a * ax + b * bx == X and a * ay + b * by == Y:
    return a * 3 + b
  return 0
    
ans = 0
idx = 0
while True:
  try:
    a = parseButton(input())
    b = parseButton(input())
    prize = parsePrize(input())
    idx += 1
    ans += solve(a, b, prize)
    input()
  except:
    break

print(ans)