class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        count = 1
        result = 0
        if len(nums) == 0:
            return 0
        for i in range(1, len(nums),1):
            if nums[i]-nums[i-1] == 1:
                count += 1
            else:
                if count > result:
                    result = count
                count = 1
        if count > result:
            result = count
        return result



        