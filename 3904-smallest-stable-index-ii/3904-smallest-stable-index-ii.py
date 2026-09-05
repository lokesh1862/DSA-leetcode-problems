class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        r=[nums[-1]]*n
        for i in range(n-2,-1,-1):
            r[i]=min(r[i+1],nums[i])
        l=0
        for i in range(n):
            l=max(l,nums[i])
            if l-r[i]<=k:
                return i
                break
        return -1
        