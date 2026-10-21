class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        table = {}
        for num in nums:
            if num not in table.keys():
                table[num] = 1
            else:
                table[num] += 1
        counter = 0
        result = []
        while counter < k:
            max_key = max(table, key=table.get)
            result.append(max_key)
            table.pop(max_key)
            counter += 1

        return result
