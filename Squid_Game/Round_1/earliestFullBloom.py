class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        def compare(a, b):
            a1 = max(a[0] + b[0] + b[1], a[0] + a[1])
            b1 = max(b[0] + a[0] + a[1], b[0] + b[1])
            return a1 - b1
        res = curr = 0
        for p_time, g_time in sorted(zip(plantTime, growTime), key=cmp_to_key(compare)):
            res = max(res, curr + p_time + g_time)
            curr += p_time
        return res