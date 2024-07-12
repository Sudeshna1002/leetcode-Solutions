class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        from collections import Counter
        
        if max(Counter(nums).values())>2:
            return False
        else:
            return True