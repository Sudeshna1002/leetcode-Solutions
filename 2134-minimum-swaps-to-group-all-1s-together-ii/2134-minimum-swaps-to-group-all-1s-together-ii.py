class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n=len(nums)
        total_nums=sum(nums)
        l=0
        window_ones=0
        max_window_ones=0
        for r in range(2*n):
            if nums[r%n]:
                window_ones+=1
            if r-l+1>total_nums:
                window_ones-=nums[l%n]
                l+=1
            max_window_ones=max(max_window_ones,window_ones)
        return total_nums-max_window_ones
            
        