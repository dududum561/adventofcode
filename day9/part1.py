diskMap = [int(x) for x in list(input())]

mem = []
for i in range(len(diskMap)):
  if i % 2 == 0:
    id = i // 2
    mem.extend([id] * diskMap[i])
  else:
    mem.extend(['.'] * diskMap[i])

dotsCnt = mem.count('.')
digitCnt = len(mem) - dotsCnt

opCnt = 0
for i in range(digitCnt, len(mem)):
  opCnt += mem[i] != '.'

def getLastEntry():
  ptr = len(mem) - 1
  while mem[ptr] == '.':
    ptr -= 1
  return ptr

def getFirstEmptyEntry():
  for ptr in range(len(mem)):
    if mem[ptr] == '.':
      return ptr


lastEntry = getLastEntry()
firstEmptyEntry = getFirstEmptyEntry()

for i in range(opCnt):
  mem[firstEmptyEntry], mem[lastEntry] = mem[lastEntry], mem[firstEmptyEntry]
  while firstEmptyEntry < lastEntry:
    ok = False
    if mem[firstEmptyEntry] != '.':
      firstEmptyEntry += 1
      ok = True
    if mem[lastEntry] == '.':
      lastEntry -= 1
      ok = True
    if not ok: break
  if firstEmptyEntry >= lastEntry: break

ans = 0
for i in range(digitCnt):
  ans += i * int(mem[i])
print(ans)