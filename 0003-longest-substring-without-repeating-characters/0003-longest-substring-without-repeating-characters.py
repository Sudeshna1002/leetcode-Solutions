class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            sett=set()
            result=0
            l=0
            r=0
            for r in range(len(s)):
                while s[r] in sett:
                    sett.remove(s[l])
                    l=l+1
                sett.add(s[r])
                result=max(result,r-l+1)
            return result
