class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j = len(numbers) - 1
        i = 0
        left = numbers[i]
        right = numbers[j]
        while left+right != target and i < len(numbers) and j >= 0:
            if(left + right > target):
                j -= 1
                right = numbers[j]
            else:
                i += 1
                left = numbers[i]
        return [i+1, j+1]
        

        