class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        list1 = nums[0:len(nums)-1]
        list2 = nums[1:len(nums)]
        prev1, prev2, prev3, prev4 = 0, 0, 0, 0

        for n in list1:
            temp = max(prev2 + n, prev1)
            prev2 = prev1
            prev1 = temp
            
        for n in list2:
            temp = max(prev4+n, prev3)
            prev4 = prev3
            prev3 = temp

        return max(prev3, prev1)
    

        


    

