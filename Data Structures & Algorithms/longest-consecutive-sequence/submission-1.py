class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        starts = set()
        length = 0
        for num in nums:
            if num-1 not in mySet:
                starts.add(num)
        for num in starts:
            currentLength = 1
            while num+1 in mySet:
                currentLength += 1
                num += 1
            if currentLength > length:
                length = currentLength
        return length