class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxDeque = collections.deque()
        minDeque = collections.deque()
        i = 0
        for num in nums:
            while len(maxDeque) and num > maxDeque[-1]:
                maxDeque.pop()
            while len(minDeque) and num < minDeque[-1]:
                minDeque.pop()
            maxDeque.append(num)
            minDeque.append(num)
            if maxDeque[0] - minDeque[0] > limit:
                if maxDeque[0] == nums[i]: maxDeque.popleft()
                if minDeque[0] == nums[i]: minDeque.popleft()
                i += 1
        return len(nums) - i

print(longestSubarray([8,2,4,7],4))
print(longestSubarray([10,1,2,4,7,2],5))
print(longestSubarray([4,2,2,2,4,4,2,2],0))
