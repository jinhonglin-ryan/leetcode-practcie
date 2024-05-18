class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        # anagram str -> a list of anagrams strings
        sorted_str_to_index = {}
        res = []
        for s in strs: 
            # use sorted(s) as the key 
            s_sorted = str(sorted(s))
            if s_sorted in sorted_str_to_index:
                # a list += a list is still a list with s appended at the end
                sorted_str_to_index[s_sorted] += [s]
            else:
                sorted_str_to_index[s_sorted] = [s]
                
        for sorted_s in sorted_str_to_index:
            res += [sorted_str_to_index[sorted_s]]
        return res 