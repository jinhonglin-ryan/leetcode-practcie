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
        
        sorted_str_to_index = defaultdict(list)

        # 填充字典
        for i, s in enumerate(strs):
            s_sorted = tuple(sorted(s))  # 使用元组作为键
            sorted_str_to_index[s_sorted].append(s)  # 直接存储字符串

        # 初始化结果列表
        res = []

        # 遍历字典并构建结果
        for anagrams in sorted_str_to_index.values():
            res.append(anagrams)

        return res