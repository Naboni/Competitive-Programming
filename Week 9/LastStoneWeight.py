class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
        while len(stones) > 1:
            stone_1, stone_2 = heapq.heappop(stones), heapq.heappop(stones)
            if stone_1 != stone_2:
                heapq.heappush(stones,stone_1-stone_2)
        if not stones:
            return 0
        return -stones[0]
