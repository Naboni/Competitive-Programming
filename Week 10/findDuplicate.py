class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast, finder = 0, 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                while slow != finder:
                    slow = nums[slow]
                    finder = nums[finder]
                return finder
