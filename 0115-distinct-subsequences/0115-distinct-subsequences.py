class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        c={}
        def dfs(i,j):
            if j==len(t):
                return 1
            if i==len(s):
                return 0
            if (i,j) in c:
                return c[(i,j)]
            if s[i]==t[j]:
                c[(i,j)]=dfs(i+1,j+1)+dfs(i+1,j)
            else:
                c[(i,j)]=dfs(i+1,j)
            return c[(i,j)]
        return dfs(0,0)
        