dictionary = set([s for s in input().strip().split(", ")])
words = []

maxLen = 0
for s in dictionary: maxLen = max(maxLen, len(s))

input()
while True:
  try:
    word = input().strip()
    words.append(word)
  except:
    break

def calc(s):
  dp = [-1 for x in range(len(s))]
  def go(i):
    if i > len(s): return 0
    if i == len(s): return 1
    if dp[i] != -1: return dp[i]
    ans = 0
    for length in range(1, maxLen + 1):
      if s[i:i+length] in dictionary:
        ans += go(i + length)
    dp[i] = ans
    return ans
  return go(0)

ans = 0
for word in words:
  ans += calc(word)
print(ans)