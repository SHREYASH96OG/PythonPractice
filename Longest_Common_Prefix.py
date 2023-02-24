# # 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

# solution-->
class Solution:
    def longestCommonPrefix(self, S: List[str]) -> str:
        if "" in S or S == []:
            return ""
        preix = S[0]
        for i in range(1,len(S)):
            while(preix != ""):
                try:
                    if str.index(str(S[i]),preix) == 0:
                        break
                    else:
                        preix = preix[:-1]
                except:
                    
                    preix = preix[:-1]
        return preix
        
