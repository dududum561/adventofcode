nums = [int(x) for x in input().split()]
ITERS = 75

memo = dict()
def calc(x, iters):
  if iters == 0: return 1
  if (x, iters) in memo: return memo[(x, iters)]
  ans = 0
  if x == 0:
    ans = calc(1, iters - 1)
  elif len(str(x)) % 2 == 0:
    s = str(x)
    half = len(s) // 2
    l, r = int(s[0:half]), int(s[half:])
    ans = calc(l, iters - 1) + calc(r, iters - 1)
  else:
    ans = calc(x * 2024, iters - 1)
  memo[(x, iters)] = ans
  return ans

ans = 0
for x in nums:
  ans += calc(x, ITERS)
print(ans)