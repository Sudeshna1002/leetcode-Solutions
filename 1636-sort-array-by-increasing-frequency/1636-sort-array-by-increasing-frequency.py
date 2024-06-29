class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        from collections import Counter
        x=Counter(nums)
        freq=list(x.values())
        maximum=max(freq)
        num_1=[]
        for i in range(len(nums)-1,0,-1):
            for j in range(i):
                if nums.count(nums[j])>nums.count(nums[j+1]):
                    nums[j],nums[j+1]=nums[j+1],nums[j]
                elif nums.count(nums[j])==nums.count(nums[j+1]):
                    if nums[j+1]>nums[j]:
                        nums[j],nums[j+1]=nums[j+1],nums[j]
                    

        
        return nums   
            