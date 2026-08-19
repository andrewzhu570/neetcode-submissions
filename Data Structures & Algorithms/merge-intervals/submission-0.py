class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        current = intervals[0]

        if len(intervals) == 1:
            return intervals

        for i in range(1, len(intervals)):
            if current[1] < intervals[i][0]:
                res.append(current)
                current = intervals[i]

                if i == len(intervals)-1:
                    break
                    
                continue
            
            current[1] = max(current[1], intervals[i][1])

        res.append(current)
        return res