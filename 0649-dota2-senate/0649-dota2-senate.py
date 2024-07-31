class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        
        # 队列
        # 每一个人都是移出离自己最近的对方阵营的人
        # 用循环队列
        
        r = deque()
        d = deque()
        
        # 初始化双方阵营的投票顺序
        for i in range(len(senate)):
            if senate[i] == 'R':
                r.append(i)
            else:
                d.append(i)
        
        n = len(senate)
        # 只要都还有人能投票，就继续循环       
        while r and d:
            if r[0] < d[0]:
                r.append(r[0] + n) # +n是因为这代表了下一轮的投票顺序
            else:
                d.append(d[0] + n)
            r.popleft()
            d.popleft()
                
        if r:
            return "Radiant"
        else:
            return "Dire"
            
            
                
                    
                