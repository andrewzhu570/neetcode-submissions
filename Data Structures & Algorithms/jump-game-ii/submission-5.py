class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        l = 0 
        r = l + nums[l]
        count = 1
        while r < len(nums)-1 and r > l:
            max_index = -1
            for i in range(l+1, r+1):
                if max_index == -1:
                    max_index = i
                else:
                    if i + nums[i] >= max_index + nums[max_index]:
                        max_index = i
            count += 1
            l = max_index
            r = l + nums[l]
        return count
