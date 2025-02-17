# platform - leetcode
#link - https://leetcode.com/problems/group-anagrams/
# concept - grouping anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        for i in strs:
            str1 = ''.join(sorted(i))
            if str1 in dict1:
                dict1[str1].append(i) 
            else:
                dict1[str1] = [i]  
        return list(dict1.values())
