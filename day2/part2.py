ans = 0
while True:
  try:
    _row = [int(x) for x in input().split()]
    for removeIdx in range(len(_row)):
      valid = True
      row = _row[:removeIdx] + _row[removeIdx+1:]
      idiff = row[0] - row[1]
      if abs(idiff) < 1 or abs(idiff) > 3:
        valid = False
        continue
      idiff = idiff < 0
      for i in range(1, len(row)):
        diff = row[i - 1] - row[i]
        if abs(diff) < 1 or abs(diff) > 3:
          valid = False
          break
        diff = diff < 0
        valid = valid and diff == idiff
      ans += valid
      if valid:
        break
  except:
    break
  
print(ans)