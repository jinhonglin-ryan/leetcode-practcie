# https://blog.csdn.net/fuxuemingzhu/article/details/79388432

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
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        if curr.isWord == False:
            return False
        return True

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)