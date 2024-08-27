class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #first step of a two pointers problem
        nums.sort()
        result = []

        #we set fixed the position i and we move across the list
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:  #if nums[i] is the same as the previous, we would find the same triplets, so we skip
                continue

            left, right = i + 1, len(nums) - 1 #two pointers problem, so we take the first element and the last
            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]

                if currentSum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:  # We check if the next left is a duplicate, in that case, we skip it
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:  # We check if the next right is a duplicate, in that case, we skip it
                        right -= 1
                    left += 1
                    right -= 1
                elif currentSum < 0: #the sum is lower than 0, so we have to move from left
                    left += 1
                else: #the sum is exceeding 0, so we have to move from right
                    right -= 1

        return result