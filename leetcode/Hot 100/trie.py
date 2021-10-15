class trieNode:
    def __init__(self):
        self.next = {None:trieNode}
        self.is_word = False
class Trie:
    def __init__(self):
        self.Node = trieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.Node
        for s in word:
            node = node.next[s]
        node.is_word = True
    def search(self,word):
        node  = self.Node
        for s in word:
            if s not in node.next:
                return False
            else:
                node = node.next[s]
        return node.is_word

Node = Trie()
Node.insert("apple")
a = Node.search("apple")
print(a)








## way -2
# class trie:
#     def __init__(self):
#         self.node = {}
#
#     def insert(self,word):
#         trie1 = self.node
#         for i in word:
#             if i not in trie1:
#                 trie1[i] = {}
#             trie1 = trie1[i]
#         trie1["end"] = "end"
#
#     def search(self,word):
#         trie1 = self.node
#         for a in word:
#             if a not in trie1:
#                 return False
#             trie1 = trie1[a]
#         if 'end' in trie1:
#             return True
#         return False
#
#     def startsWith(self,prefix):
#         trie1 = self.node
#         for a in prefix:
#             if a not in trie1:
#                 return False
#             trie1 = trie1[a]
#         return True
#
# trie2 = trie()
# trie2.insert('apple')
# a = trie2.search('apple')
# print(a)


