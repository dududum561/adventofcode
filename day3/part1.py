def checkNum(x):
  try:
    if int(x) < 0:
      return False
    for ch in x:
      o = ord(ch)
      if o < ord('0') or o > ord('9'):
        return False
  except:
    return False
  return True

ans = 0
while True:
  try:
    for token in input().split("mul")[1:]:
      try:
        if token[0] != '(':
          continue
        token = token[1:token.find(')')]
        x, y = token.split(',')
        if not checkNum(x) or not checkNum(y):
          continue
        x = int(x)
        y = int(y)
        ans += x * y
      except:
        continue
  except:
    break
print(ans)