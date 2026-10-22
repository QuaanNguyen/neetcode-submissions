import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = math.prod(nums)
        result = []
        for i in range(len(nums)):
            if nums[i] == 0:
                clean_nums = nums.copy()
                clean_nums.pop(i)
                result.append(int(math.prod(clean_nums)))
            else:
                result.append(int(total/nums[i]))
        return result