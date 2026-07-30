class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        for i in range(len(position)):
            position[i] = [position[i], speed[i]]

        position.sort(reverse=True)
        stack = []
        stack.append(position[0])

        for i in range(1, len(position)):
            stack_time = (target - stack[len(stack)-1][0]) / stack[len(stack)-1][1]
            this_time = (target - position[i][0]) / position[i][1]

            if this_time > stack_time:
                stack.append(position[i])

        return len(stack)
        ## stack = [[7,1]]
        ##[[7, 1], [4, 2], [1, 2], [0,1]]