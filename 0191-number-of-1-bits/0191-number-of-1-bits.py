class Solution:
    def hammingWeight(self, n: int) -> int:
        arr=[]
        while n>=1:
            arr.append(n%2)
            n=n//2
        return arr.count(1)
        