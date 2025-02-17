nums = [int(x) for x in input().split()]

def transform(nums):
  newNums = []
  for x in nums:
    if x == 0:
      newNums.append(1)
    elif len(str(x)) % 2 == 0:
      s = str(x)
      l, r = s[0 : len(s) // 2], s[len(s) // 2 :]
      newNums.append(int(l))
      newNums.append(int(r))
    else:
      newNums.append(x * 2024)
  return newNums

for iter in range(25):
  nums = transform(nums)

print(len(nums))