class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = sys.maxsize #Set to maximum on purpose
        wsum = 0
        left = 0

        for right in range(len(nums)):
            wsum += nums[right] #Sum the number on the right

            while wsum >= target: #if the sum exceeds the target, shrink the array from the left
                min_length = min(min_length, right-left+1)
                wsum -= nums[left] #we can subtract the left number
                left += 1

        return 0 if min_length == sys.maxsize else min_length