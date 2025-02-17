from functools import cmp_to_key


relation = {}
while True:
  condition = input()
  if "|" not in condition:
    break
  x, y = (int(x) for x in condition.split("|"))
  if x not in relation:
    relation[x] = set()
  relation[x].add(y)

ans = 0

while True:
  try:
    order = [int(x) for x in input().split(",")]
  except:
    break
  def canReach(x, y):
    if x not in relation: return False
    return y in relation[x]
  def checkValid():
    for i in range(len(order)):
      for j in range(i + 1, len(order)):
        if canReach(order[j], order[i]):
          return False
    return True
  if checkValid():
    continue
  def compareFunc(x, y):
    if y in relation and x in relation[y]:
      return +1
    if x in relation and y in relation[x]:
      return -1
    return 0
  order = sorted(order, key = cmp_to_key(compareFunc))
  if checkValid():
    ans += order[len(order) // 2]

print(ans)