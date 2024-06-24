class Node(object):
    def __init__(self):
        self.children = {}
        self.isWord = False
        
class Trie(object):
    def __init__(self):
        self.root = Node()
        
    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]
        curr.isWord = True
    
    def search(self, word):
        def dfs(index, node):
            # 如果已经搜完了，return当前node的isWord
            if index == len(word):
                return node.isWord 
            
            # 还没搜完的话, 取出当前字符，分成两种情况讨论，是. 和 非.
            ch = word[index]
            
            if ch == ".":
                # 如果当前字符是. , 则对当前node下的所有child Node 进行搜索
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
            else:
                # 字符不是., 正常search 
                if ch not in node.children:
                    return False
                
                child = node.children[ch]
                
                if dfs(index + 1, child):
                    return True
            # 如果上面都没有return True，表示没搜到，return False    
            return False
        
        # 从root开始搜
        return dfs(0, self.root)
                            
class WordDictionary(object):

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        self.trie.insert(word)
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return self.trie.search(word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)