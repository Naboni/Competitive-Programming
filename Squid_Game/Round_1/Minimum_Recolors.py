class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = inf
        hashmap = defaultdict(int)
        left = 0
        for right in range(len(blocks)):
            hashmap[blocks[right]] += 1
            if right - left + 1 > k:
                hashmap[blocks[left]] -= 1
                left += 1
            if right - left + 1 == k:
                res = min(res, hashmap["W"])
        return res