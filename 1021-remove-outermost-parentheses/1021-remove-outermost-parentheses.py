class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        d=0
        res=''
        for i in s:
            if i=='(':
                d+=1
            else:
                d-=1
            if (i=='(' and d==1) or (i==')' and d==0):
                continue
            else:
                res+=i
        return res
        