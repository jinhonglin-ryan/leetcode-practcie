class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        
        # 思路：收到20的时候，优先使用一个 10 美元和一个 5 美元找零，这样保证有够多5，后续找零更灵活
        if bills[0] != 5:
            return False
        
        fives = 0
        tens = 0
        
        for bill in bills:
            if bill == 5:
                fives += 1
                
            elif bill == 10:
                tens += 1
                if fives < 1:
                    return False 
                fives -= 1
                
            elif bill == 20:
                if tens > 0 and fives > 0:
                    tens -= 1
                    fives -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
        
        return True