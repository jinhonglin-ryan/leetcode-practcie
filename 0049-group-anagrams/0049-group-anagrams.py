class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        sorted_str_to_index = {}
        res = []
        for s in strs:
            s_sorted = str(sorted(s))
            if s_sorted in sorted_str_to_index:
                sorted_str_to_index[s_sorted] += [s]
            else:
                sorted_str_to_index[s_sorted] = [s]
                
        for sorted_s in sorted_str_to_index:
            res += [sorted_str_to_index[sorted_s]]
        return res 