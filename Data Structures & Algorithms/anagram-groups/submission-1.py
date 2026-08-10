class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]
        table = {}
        for each in strs:
            key = tuple(sorted(each))
            if key not in table:
                table[key] = [each]
            else:
                table[key].append(each)
        return list(table.values())
        