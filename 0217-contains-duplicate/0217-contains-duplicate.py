class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      from collections import Counter
      x=Counter(nums)
      max_count=max(x.values())
      if max_count>1:
        return True
      else :
            return False
    