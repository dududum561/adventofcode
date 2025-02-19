registers = [0, 0, 0]
for i in range(3):
  x = int(input().split(": ")[1])
  registers[i] = x

input()
instructions = [int(x) for x in input().strip().split(": ")[1].split(",")]

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
    result.append(str(out(i)))
    i += 2
  if ins == 6:
    bdv(i)
    i += 2
  if ins == 7:
    cdv(i)
    i += 2

print(','.join(result))