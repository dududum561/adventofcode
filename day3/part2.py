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
enabled = True
while True:
  try:
    for token in input().split("mul"):
      otoken = token
      try:
        if token[0] != '(':
          raise
        token = token[1:token.find(')')]
        x, y = token.split(',')
        if not checkNum(x) or not checkNum(y):
          raise
        x = int(x)
        y = int(y)
        if enabled:
          ans += x * y
      except:
        pass
      finally:
        token = otoken
        lastDo = token.rfind("do()")
        lastDont = token.rfind("don't()")
        lastIdx = max(lastDo, lastDont)
        if lastIdx != -1:
          enabled = lastDo == lastIdx
  except:
    break
print(ans)