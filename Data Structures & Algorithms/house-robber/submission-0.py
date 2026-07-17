class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1, prev2 = 0, 0

        for n in nums:
            temp = max(prev2 + n, prev1)
            prev2 = prev1
            prev1 = temp
            
        return prev1
    

        


    

