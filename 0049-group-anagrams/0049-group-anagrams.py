class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
#         sorted_str_to_index = {}
#         for i, s in enumerate(strs):
#             s_sorted = str(sorted(s))
#             if s_sorted in sorted_str_to_index:
#                 sorted_str_to_index[s_sorted].append(i)
#             else: 
#                 sorted_str_to_index[s_sorted] = [i]
        
#         res = defaultdict(list)
        
#         for anagrams, indices in sorted_str_to_index.items():
#             for idx in indices:
#                 res[anagrams].append(strs[idx])
        
#         return list(res.values()) 
        
        str_dict = dict()
        res = []
        for s in strs:
            sort_s = str(sorted(s))
            if sort_s in str_dict:
                str_dict[sort_s] += [s]
            else:
                str_dict[sort_s] = [s]

        for sort_s in str_dict:
            res += [str_dict[sort_s]]
        return res