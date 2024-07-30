class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        occurrences = defaultdict(int)
        
        for num in arr:
            occurrences[num] += 1
        
        x = set()
        
        for _, value in occurrences.items():
            if value in x:
                return False
            
            x.add(value)
            
        return True
            
        