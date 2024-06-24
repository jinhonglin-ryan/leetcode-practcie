class Trie:

    def __init__(self):
        self.children = {}
        self.isEnd = False

    def insert(self, word):
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
        cur.isEnd = True

    def search(self, word):
        cur = self
        for i, ch in enumerate(word):
            if ch == '.':
                return any(child.search(word[i + 1:]) for child in cur.children.values())
            if ch not in cur.children:
                return False
            cur = cur.children[ch]
        return cur.isEnd


class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word):
        self.trie.insert(word)

    def search(self, word):
        return self.trie.search(word)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)