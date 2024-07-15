class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        
        # 类似分发糖果，要考虑两个维度
        # 先按照身高从大到小排序，且如果身高相同的话，k按从小到大排序，这样保证了第i个人的前面的人都比第i个人高，且k值是合法的
        # 比如 7,0 和 7,1 我们要求7,0 排在7,1前面，这样才合法
        # 接下来遍历people，对k的值进行处理，插入到排序后对应的位置即可 
        
        people.sort(key=lambda x: (-x[0], x[1]))
        
        queue = []
        
        for person in people:
            queue.insert(person[1], person)
            
        return queue 