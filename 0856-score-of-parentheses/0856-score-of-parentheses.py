class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        d=0
        prev=''
        res=0
        for i in s:
            if i=='(':
                d+=1
            else:
                d-=1
                if prev=='(':
                    res+=2**d
            prev=i
        return res