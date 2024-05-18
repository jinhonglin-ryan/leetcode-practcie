class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
#         # anagram str -> a list of anagrams strings
#         sorted_str_to_index = {}
#         res = []
#         for s in strs: 
#             # use sorted(s) as the key 
#             s_sorted = str(sorted(s))
#             if s_sorted in sorted_str_to_index:
#                 # a list += a list is still a list with s appended at the end
#                 sorted_str_to_index[s_sorted] += [s]
#             else:
#                 sorted_str_to_index[s_sorted] = [s]
                
#         for sorted_s in sorted_str_to_index:
#             res += [sorted_str_to_index[sorted_s]]
#         return res 

        anagrams = defaultdict(list)
    
        # 填充字典
        for s in strs:
            # 将字符串排序并转换为字符串作为键
            sorted_str = ''.join(sorted(s))
            # 将原始字符串添加到对应键的值列表中
            anagrams[sorted_str].append(s)

        # 将结果从 defaultdict 转换为普通列表列表
        return list(anagrams.values())