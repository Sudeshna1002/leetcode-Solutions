# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        arr=[]
        sum=0
           
        while head:
            arr.append(head.val)
            head=head.next
       
        for i in range(len(arr)):
            sum=sum+arr[i]*(2**(len(arr)-1-i))
        
        return sum
      

            
        
        