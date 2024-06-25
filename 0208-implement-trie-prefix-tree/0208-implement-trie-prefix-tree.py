# https://blog.csdn.net/fuxuemingzhu/article/details/79388432
# root节点不存任何信息
# 一个节点curr下有一个children map，map from a 字符 to a Node, curr.children[c] 就是到了这个node下

class Node(object):
    def __init__(self):
        self.children = {} # map from 字符 to node
        self.isWord = False

class Trie(object):

    def __init__(self):
        self.root = Node()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root # 从root开始insert
        for c in word: # 存下每一个字符
            if c not in curr.children: # 如果当前节点的children字典里还没有该字符
                curr.children[c] = Node() # 为这个children下的字典对应的字符创建一个Node
            curr = curr.children[c] # curr move to this new Node
        curr.isWord = True # 遍历完所有字符in word之后，表示完成了插入，此时curr指向最后一个字符的node，标记当前node isWord为True，表示从root出发走到这个位置是一个Trie中的Word
        
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self.root # 从root开始搜
        for c in word: # 遍历word中的每一个字符 
            if c not in curr.children: # 如果当前的字符不在当前node的child字典里，说明之前insert的时候没有创建过对于这个字符的Node，那么这个Trie 中就是没有这个word，所以直接return False
                return False 
            curr = curr.children[c] # 如果当前字符在当前node child字典里，则我们去到这个node进行下一个字符的检查
        if curr.isWord == False: # 当遍历完所有字符的时候，如果当前node的isWord是False，则也是没有这个Word，return False
            return False
        return True

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self.root # 也是从root开始搜
        for c in prefix: # 遍历每一个字符 
            if c not in curr.children: # 如果当前字符并不在当前node的child字典里，同insert，热屯 False
                return False
            curr = curr.children[c] # 迭代到下一个Node
        return True # 遍历完所有字符后，我们可以直接return True，因为只是要查看是否有startwith这个prefix的存在，而不是整个Word
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)