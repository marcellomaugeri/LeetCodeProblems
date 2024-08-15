# This solution is not efficient enough to pass the last test case.
#class Solution:
#    def smallestDistancePair(self, nums: List[int], k: int) -> int:
#        distances = []
#        for i in range(len(nums)-1):
#            for j in range(i+1, len(nums)):
#                distances.append(abs(nums[i] - nums[j]))
#        distances.sort()
#        return distances[k-1]

from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort() #Sort the array
        n = len(nums) #Length of the array
        left = 0 #Theoretically smallest distance
        right = nums[-1] - nums[0] #Max distance
        
        while left < right:
            mid = (left + right) // 2  #Calculate the mid distance (which is the floor of the average of left and right)
            count = 0 #Count of the number of pairs with distance <= mid
            j = 0

            for i in range(n):
                while j < n and nums[j] - nums[i] <= mid:
                    j += 1
                count += j - i - 1 
                
            if count < k: 
                left = mid + 1
            else:
                right = mid
        return left 
            