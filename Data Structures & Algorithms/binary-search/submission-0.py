class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(arr, offSet):
            if not arr:
                return -1
            midPoint = len(arr) // 2
            if target == arr[midPoint]:
                return offSet + midPoint
            if target > arr[midPoint]:
                return binarySearch(arr[midPoint+1:], offSet + midPoint + 1)
            else:
                return binarySearch(arr[:midPoint], offSet)
        return binarySearch(nums, 0)
            



