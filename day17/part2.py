_registers = [0, 0, 0]
for i in range(3):
  x = int(input().split(": ")[1])
  _registers[i] = x

input()
instructions = [int(x) for x in input().strip().split(": ")[1].split(",")]

def simulate(aval, minLen=-1):
  registers = _registers.copy()
  registers[0] = aval

  def getComboOpValue(op):
    if 0 <= op and op <= 3: return op
    if 4 <= op and op <= 6: return registers[op - 4]
    raise Exception()

  def _adv(i, storageIdx):
    num = registers[0]
    pw = getComboOpValue(instructions[i + 1])
    if pw > 100: pw = 100
    den = 1 << pw
    registers[storageIdx] = num // den

  def adv(i):
    _adv(i, 0)

  def bxl(i):
    registers[1] ^= instructions[i + 1]

  def bst(i):
    opValue = getComboOpValue(instructions[i + 1])
    res = opValue % 8
    registers[1] = res

  def jnz(i):
    if registers[0] == 0: return i + 2
    return instructions[i + 1]

  def bxc():
    registers[1] ^= registers[2]

  def out(i):
    opValue = getComboOpValue(instructions[i + 1])
    return opValue % 8

  def bdv(i):
    _adv(i, 1)

  def cdv(i):
    _adv(i, 2)

  result = []

  i = 0
  idx = 0
  while i < len(instructions):
    ins = instructions[i]
    if ins == 0:
      adv(i)
      i += 2
    if ins == 1:
      bxl(i)
      i += 2
    if ins == 2:
      bst(i)
      i += 2
    if ins == 3:
      i = jnz(i)
    if ins == 4:
      bxc()
      i += 2
    if ins == 5:
      result.append(out(i))
      idx += 1
      i += 2
      if minLen != -1 and idx == minLen: return result
    if ins == 6:
      bdv(i)
      i += 2
    if ins == 7:
      cdv(i)
      i += 2
  return result

pw = 0
buckets = []

# B = (A % 8) xor 1 xor (A >> (A % 8 ^ 2) % 8)

for instruction in instructions:
  bucket = []
  for block in range(1 << 10):
    nB = (block & 7) ^ 1 ^ ((block >> ((block & 7) ^ 2)) & 7)
    if nB == instruction:
      A = block << pw
      bucket.append(A)
  pw += 3
  buckets.append(bucket)

def matchPrefix(seq):
  for i in range(min(len(seq), len(instructions))):
    if seq[i] != instructions[i]:
      return i
  return min(len(seq), len(instructions))

candidates = buckets[0]

prefixLen = 2
pw = 3
for bucket in buckets[1:]:
  print(len(candidates), len(bucket))
  newCandidates = []
  for y in candidates:
    yPrefix = y & ~((1 << pw) - 1)
    for x in bucket:
      z = x | y
      if x & yPrefix != yPrefix: continue
      res = simulate(z, prefixLen)
      if matchPrefix(res) >= prefixLen and len(simulate(z)) <= len(instructions):
        newCandidates.append(z)
  newCandidates.sort()
  candidates = newCandidates[:100]
  prefixLen += 1
  pw += 3

for A in candidates[:10]:
  print(A, simulate(A))