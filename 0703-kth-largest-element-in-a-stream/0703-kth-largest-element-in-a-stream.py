class KthLargest(object):
    
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        # Heapq解法：维护一个大小为k的最小堆（其中存放了nums中最大的k个数，堆顶为这k个数中的最小数）
        # 用list min_heap 来代表最小堆 
        # 1. 
        # heapq.heappush 用于将一个元素添加到堆中，并维持堆的性质。
        # 添加：元素首先被添加到列表（堆）的末尾。
        # 调整：为了维护堆的性质（在最小堆中，任何给定节点的值都必须小于或等于其子节点的值），新添加的元素可能需要向上移动。这个过程称为上浮（percolate up）或向上调整。
        # 向上调整：新元素与其父节点比较（在列表中的位置为 (index - 1) // 2），如果新元素小于其父节点，则它们的位置会交换。这个比较-交换过程会一直持续，直到新元素要么到达列表的顶部（成为新的堆顶），要么其父节点不再大于它。
        
        # 2.
        # heapq.heappop 用于移除并返回堆中的最小元素（堆顶元素）。
        # 移除：堆顶元素（列表的第一个元素）被移除并保存，以便最后返回。
        # 替换：堆中的最后一个元素被移动到堆顶（列表的开始）。
        # 调整：为了重新维护堆的性质，这个新的堆顶元素可能需要向下移动。这个过程称为下沉（percolate down）或向下调整。
        # 向下调整：新的堆顶元素与其子节点（在列表中的位置为 2 * index + 1 和 2 * index + 2）比较，如果它大于任何一个子节点，它会与最小的子节点交换位置。这个比较-交换过程会一直持续，直到新的堆顶元素小于其所有子节点或成为叶子节点。
        
        
        self.nums = nums
        self.k = k
        self.min_heap = []
        for num in nums:
            heapq.heappush(self.min_heap, num)
            if len(self.min_heap) > k:
                # 如果加入一个数之后，最小堆的大小大于k了，需要移除这个最小堆的最小值，也就是堆顶，来保障最小堆依旧是k个数
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