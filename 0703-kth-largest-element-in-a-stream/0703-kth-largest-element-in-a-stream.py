class KthLargest(object):
    
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        # Heapq解法：维护一个大小为k的最小堆
        self.nums = nums
        self.k = k
        self.min_heap = []
        for num in nums:
            heapq.heappush(self.min_heap, num)
            if len(self.min_heap) > k:
                heapq.heappop(self.min_heap)
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)