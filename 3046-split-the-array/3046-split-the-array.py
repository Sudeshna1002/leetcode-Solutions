class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        from collections import Counter
        nums1=[]
        nums2=[]
        if max(Counter(nums).values())>2:
            return False
           
        for num in nums:
            if len(nums1)==len(nums)/2:
                nums2.append(num)
            elif len(nums2)==len(nums)/2:
                nums1.append(num)
            else:    
                if num not in nums1:
                    nums1.append(num)
         
                elif num not in nums2:
                    nums2.append(num)
               
                else:
                    return False
        return len(nums1) == len(nums2) == len(nums) // 2