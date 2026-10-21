class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        
        if not nums:
            return 0
        
        curr = 1
        res = 1
        for i in range(1, len(nums)):
            if nums[i]-nums[i-1] == 1:
                curr += 1
            else:
                curr = 1
            res = max(res, curr)
        return res



        