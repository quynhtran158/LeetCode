class Solution:
  def arrangeCoins(self, n: int) -> int:
    remain = n
    if n == 1:
      return 1
    else:
      remain -= 1
      count = 1
      for r in range(2, n+1):
        if remain >= r:
          remain -= r
          count += 1
        else:
           return count 