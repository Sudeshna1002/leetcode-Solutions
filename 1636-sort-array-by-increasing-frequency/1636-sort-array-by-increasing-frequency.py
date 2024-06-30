class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        from collections import Counter
        result=[]
        counts=Counter(sorted(nums)).most_common()[::-1]
        for i,j in counts:
            result.extend(i for k in range(j))
        return result