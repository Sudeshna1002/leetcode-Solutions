class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr=[]
        for i in range(1,n+1):
            arr.append(i)
        index=0
        while len(arr)!=1:
                index=index+k-1
                while index>=len(arr):  
                  index=index-len(arr)
                arr.remove(arr[index])
        return arr[0]
                
            
            