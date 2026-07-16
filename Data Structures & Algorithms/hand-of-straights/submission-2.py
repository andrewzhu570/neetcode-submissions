class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        map = {}
        for n in hand:
            map[n] = 1 + map.get(n, 0)
        minH = list(map.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in map:
                    return False
                map[i] -= 1
                if map[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True

                



