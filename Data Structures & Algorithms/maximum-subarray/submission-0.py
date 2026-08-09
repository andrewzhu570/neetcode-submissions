class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        res = nums[0]

        for num in nums:
            curSum = max(curSum + num, num)
            res = max(curSum, res)

        
        return res

    