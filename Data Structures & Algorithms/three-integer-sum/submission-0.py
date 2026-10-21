class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for firstNum in range(len(nums)):
            for secondNum in range(firstNum+1, len(nums), 1):
                for thirdNum in range(secondNum+1, len(nums),1):
                    if nums[firstNum] + nums[secondNum] + nums[thirdNum] == 0 and [nums[firstNum], nums[secondNum], nums[thirdNum]] not in result:
                        result.append([nums[firstNum], nums[secondNum], nums[thirdNum]]) 
        return result 