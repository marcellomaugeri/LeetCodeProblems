# [108 - Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree)
### Difficulty: Easy

### Problem Statement

Given an integer array `nums` where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

#### Example 1:
```
![Example 1](image.png)
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:
![Alternative solution to Example 1](image-1.png)
```
Then the 1st smallest distance pair is (1,1), and its distance is 0.
#### Example 2:
```
![Example 2](image-2.png)
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
```

#### Constraints:
```
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
```