class Solution:
  def arrangeCoins(self, n: int) -> int:
    count = 0
    remain = n
    while remain >= count +1:
      count += 1
      remain -= count
    return count