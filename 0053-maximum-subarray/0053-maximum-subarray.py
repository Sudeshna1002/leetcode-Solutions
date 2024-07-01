class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum=0
        maximum_sum=nums[0]
        for i in nums:
            if current_sum<0:
                current_sum=0
            
            current_sum=current_sum+i
            maximum_sum=max(maximum_sum,current_sum)
        return maximum_sum
                
               
        