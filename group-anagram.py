# Group Anagrams
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2:

# Input: strs = ["x"]

# Output: [["x"]]
# Example 3:

# Input: strs = [""]

# Output: [[""]]
# Constraints:

# 1 <= strs.length <= 1000.
# 0 <= strs[i].length <= 100
# strs[i] is made up of lowercase English letters.

def groupAnagrams(strs):
  dic = {};
  for word in strs:
    count = [0] * 26;
    for char in word:
      count[ord(char) - ord('a')] += 1;
    
    key = tuple(count);
    if key not in dic:
      dic[key] = [];
    dic[key].append(word);
  ans = list(dic.values());
  ans.sort(key=len)
  return ans


ans = groupAnagrams(["act","pots","tops","cat","stop","hat"])
print(ans)