class Solution:
    # O((k+n)logn)
    # def topKFrequent(self, words: List[str], k: int) -> List[str]:
    #     count = {}
    #     # O(n)
    #     for word in words:
    #         count[word] = count.get(word, 0) + 1
    #     heap = []
    #     # O(nlogn)
    #     for i in count:
    #         heapq.heappush(heap, (-count[i], i))
    #     output = []
    #     # O(klogn)
    #     for i in range(k):
    #         popped = heapq.heappop(heap)
    #         output.append(popped[1])
    #     return output
    # O(nlogk)
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        class Word:
            def __init__(self, freq, word):
                self.word = word
                self.freq = freq
            def __lt__(self, other):
                if self.freq == other.freq:
                    return self.word > other.word 
                return self.freq < other.freq
        count = {}
        # O(n)
        for word in words:
            count[word] = count.get(word, 0) + 1
        heap = []
        # O(nlogk)
        for i in count:
            heapq.heappush(heap, Word(count[i], i))
            if len(heap) > k:
                heappop(heap)
        output = []
        # O(n)
        for i in range(len(heap)):
            output.append(heappop(heap).word)
        return output[::-1]
