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
  def concat(x, y):
    return int(str(x) + str(y))
  def dfs(sum, i):
    if i == len(nums): return sum == total
    if sum > total: return False
    res = False
    # add
    res = res or dfs(sum + nums[i], i + 1)
    # mult
    res = res or dfs(sum * nums[i], i + 1)
    # concat
    res = res or dfs(concat(sum, nums[i]), i + 1)
    return res
  ans += dfs(nums[0], 1) * total
print(ans)