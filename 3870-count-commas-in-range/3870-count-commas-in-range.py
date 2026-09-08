class Solution:
    def countCommas(self, n: int) -> int:
        if len(str(n))<4:
            return 0
        else:
            c=0
            for i in range(1000,n+1):
                c+=1
        return c
