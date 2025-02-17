diskMap = [int(x) for x in list(input())]

mem = []
maxid = 0
for i in range(len(diskMap)):
  if i % 2 == 0:
    id = i // 2
    maxid = id
    mem.append([id, diskMap[i]])
  else:
    mem.append(['.', diskMap[i]])

def getItemRange(id):
  for i in range(len(mem)):
    x, _ = mem[i]
    if x == id:
      return i
  raise Exception("uh oh", id)

def getFirstEmptyRange(minLength):
  for i in range(len(mem)):
    x, f = mem[i]
    if x == '.' and f >= minLength:
      return i
  return -1

for id in range(maxid, -1, -1):
  while len(mem) > 0 and mem[-1][0] == '.':
    mem.pop()
  idx = getItemRange(id)
  emptyIdx = getFirstEmptyRange(mem[idx][1])
  if emptyIdx == -1: # nothing found
    continue
  if emptyIdx > idx: # not gonna be to the left
    continue
  mem[emptyIdx][1] -= mem[idx][1]
  mem[idx][0] = '.'
  mem.insert(emptyIdx, [id, mem[idx][1]])

memstr = []
for [x, f] in mem:
  memstr.extend([x] * f)
ans = 0
for i in range(len(memstr)):
  if memstr[i] != '.':
    ans += i * int(memstr[i])
print(ans)