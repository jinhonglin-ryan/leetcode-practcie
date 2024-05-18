class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        num_count = {}
        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
        sorted_items = sorted(num_count.items(), key=lambda item: item[1], reverse=True)
    
        return [item[0] for item in sorted_items[:k]]
    
    
    """
    sorted_items = sorted(num_count.items(), key=lambda item: item[1], reverse=True)
    1. num_count.items() 返回一个包含字典所有key-value pair的视图对象（view object）。视图对象是一个包含字典项（key-value pair）的可迭代对象，其中每个元素是一个形如 (key, value) 的tuple。
    2. sorted(num_count.items(), key=lambda item: item[1], reverse=True) 对 num_count.items() 返回的键值对列表进行排序。
    3. key 是一个可选参数，用于指定一个函数，此函数用于从每个元素中提取用于比较的键。lambda item: item[1] 是一个匿名函数（lambda函数），它接受一个字典项（即形如 (key, value) 的元组），并返回元组的第二个元素（即value）。所以排序是基于字典的值而不是键进行的。
    key 参数接受一个函数作为输入。lambda item: item[1] 是这个函数，它定义了排序依据。lambda item: item[1] 表示使用字典项的值作为排序依据。所以排序是基于字典的value而不是key进行的。
    4. reverse 是一个可选参数。如果设为 True，列表元素将被倒序排列（从大到小）。默认是 False，即升序排列。

    """
    
    
    """
    [item[0] for item in sorted_items[:k]]
    1. sorted_items 是一个列表，包含按value从大到小排序的key-value pair。sorted_items[:k] 使用切片操作，获取列表中的前 k 个元素。
    2. for item in sorted_items[:k] 迭代 sorted_items 列表的前 k 个元素。item[0] 提取每个key-value pair的第一个元素（即字典的key）。
    """