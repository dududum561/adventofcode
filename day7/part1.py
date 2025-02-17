totalList = []
numsList = []

while True:
  try:
    total, nums = input().split(": ")
    totalList.append(int(total))
    numsList.append([int(x) for x in nums.split(" ")])
  except:
    break

ans = 0

for i in range(len(totalList)):
  total = totalList[i]
  nums = numsList[i]
  for mask in range(1 << (len(nums) - 1)):
    ctotal = nums[0]
    for i in range(len(nums) - 1):
      x = nums[i + 1]
      if (mask >> i) & 1 == 1: # multiply
        ctotal *= x
      else: # add
        ctotal += x
    if ctotal == total:
      ans += total
      break

print(ans)