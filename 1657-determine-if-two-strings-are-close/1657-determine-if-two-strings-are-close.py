class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        
        cnts1 = Counter(word1)
        cnts2 = Counter(word2)

        return sorted(cnts1.keys()) == sorted(cnts2.keys()) and sorted(cnts1.values()) == sorted(cnts2.values())