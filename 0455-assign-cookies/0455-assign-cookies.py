class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        
        # 贪心的策略，为了尽可能的满⾜更多的⼩孩，而且一块饼干不能掰成两半，所以我们应该尽量让胃口小的孩子吃小块饼干，这样胃口大的孩子才有大块饼干吃。
        # 先将g 和 s 从小到大排列
        # 若是饼干没了/孩子遍历完了，直接推出循环，返回count
        # count表示满意的孩子的数量
        
        count = 0 
        # 从小
        g = sorted(g)
        s = sorted(s)
        
        g = deque(g) # 支持popleft()
        s = deque(s)
        
        while g and s:
            # 先取出第一个孩子的需求（保留在数组中）
            need = g[0]
            # 直接拿出第一个cookie，因为如果最小的cookie都没法满足孩子的最小需求，那后续孩子的需求 也没法满足
            cookie = s.popleft()
            
            if cookie < need:
                # 如果cookie无法满足当前需求最小的孩子，去看下一个大小的cookie可否满足
                continue
            
            else:
                # 如果当前cookie满足当前需求最小的孩子，当前孩子被移出数组，count += 1 
                g.popleft()
                count += 1
                
        return count