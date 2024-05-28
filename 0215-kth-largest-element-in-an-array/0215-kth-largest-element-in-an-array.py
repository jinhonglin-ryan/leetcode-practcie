class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # 用heapq搞一个最大堆，对于num in nums取反再加入max_heap，从max_heap取出时，取反来恢复原先值
        
        max_heap = []
        
        for num in nums:
            num = -num
            heapq.heappush(max_heap, num)
            
        while k > 1 and max_heap:
            heapq.heappop(max_heap)
            k -= 1
        
        return -heapq.heappop(max_heap)