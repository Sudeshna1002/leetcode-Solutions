class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       left=0
       right=1
       maxi=0
       while right<len(prices):
            if prices[left]<prices[right]:
               profit=prices[right]-prices[left] 
               maxi=max(profit,maxi)
            else:
                left=right
            right+=1
       return maxi
            