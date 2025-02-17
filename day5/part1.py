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
  valid = True
  def canReach(x, y):
    if x not in relation: return False
    return y in relation[x]
  for i in range(len(order)):
    for j in range(i + 1, len(order)):
      if canReach(order[j], order[i]):
        valid = False
  if valid:
    ans += order[len(order) // 2]

print(ans)