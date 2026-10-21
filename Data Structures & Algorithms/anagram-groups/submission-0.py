class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for i in strs:
            sorted_key = "".join(sorted(i))
            result[sorted_key].append(i)

        return list(result.values())

