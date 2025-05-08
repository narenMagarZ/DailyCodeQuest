# Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

# Example 1:

# Input: nums = [1,2,2,3,3,3], k = 2

# Output: [2,3]
# Example 2:

# Input: nums = [7,7], k = 1

# Output: [7]
# Constraints:

# 1 <= nums.length <= 10^4.
# -1000 <= nums[i] <= 1000
# 1 <= k <= number of distinct elements in nums.

# solved using bucket sort algorithm

# take the length of given array


def topKFrequent(nums, k):
  dic = {};
  for i in nums:
    if i not in dic:
      dic[i] = 0;
    dic[i] += 1;
  newArr = [[] for i in range(len(nums) + 1) ];
 
  for n, c in dic.items():
    newArr[c].append(n)
  
  res = []
  for i in range(len(newArr) - 1, 0, -1):
    for j in newArr[i]:
      res.append(j);
      if(len(res) == k):
        return res

  return res;


result = topKFrequent([1,2,2,3,3,3], 2)
print(result)