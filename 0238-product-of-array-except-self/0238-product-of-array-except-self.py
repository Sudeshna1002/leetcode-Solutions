class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=0
        r=0
        result=[1]*len(nums)
        prefix=1
        postfix=1
        for i in range(len(nums)):
           result[i]=prefix
           prefix=prefix*nums[i]
        for i in range(len(nums)-1,-1,-1):
            result[i]=result[i]*postfix
            postfix=postfix*nums[i]
        return result
            