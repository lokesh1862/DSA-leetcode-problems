class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n=len(digits)
        res=set()
        for i in range(n):
            if digits[i]==0:
                continue
            for j in range (n):
                for k in range(n):
                    if j==i or k==i or k==j or digits[k]%2==1:
                        continue
                    ans=(100*digits[i])+(digits[j]*10)+digits[k]
                    res.add(ans)
        return len(res)
