class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d={}
        for i in s1:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        n=len(s1)
        for i in range(len(s2)-n+1):
            temp={}
            for j in range(i,i+n):
                if s2[j] in temp:
                    temp[s2[j]]+=1
                else:
                    temp[s2[j]]=1
            if temp==d:
                return True
                break
        return False

