class Solution(object):
    def longestCommonPrefix(self, strs):

        if not strs:
            return ""
        strs.sort()
        
        res = ""
        pair = zip(strs[0], strs[-1])
        for x, y in pair:
            if x == y:
                res += x
            else:
                break
                
        return res
