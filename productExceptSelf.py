# Products of Array Except Self
# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

# Follow-up: Could you solve it in 
# O
# (
# n
# )
# O(n) time without using the division operation?

# Example 1:

# Input: nums = [1,2,4,6]

# Output: [48,24,12,8]
# Example 2:

# Input: nums = [-1,0,1,2,3]

# Output: [0,-6,0,0,0]
# Constraints:

# 2 <= nums.length <= 1000
# -20 <= nums[i] <= 20


def productExceptSelf(nums):
  prefix = [1] * len(nums);
  for i in range(1, len(nums)):
    prefix[i] = prefix[i-1] * nums[i-1];
  
  suffix = [1] * len(nums);
  for i in range(len(nums) - 2, -1, -1):
    suffix[i] = suffix[i + 1] * nums[i + 1];

  result = [1] * len(nums);
  for i in range(len(nums)):
    result[i] = prefix[i] * suffix[i];
  return result;



result = productExceptSelf([-1, 0, 1, 2, 3]);
print(result)