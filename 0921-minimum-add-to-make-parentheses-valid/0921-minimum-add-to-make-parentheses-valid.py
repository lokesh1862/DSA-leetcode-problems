class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        st=[]
        for i in range(len(s)):
            if st and s[i]==')' and st[-1]=='(':
                st.pop()
            else:
                st.append(s[i])
        return len(st)
        