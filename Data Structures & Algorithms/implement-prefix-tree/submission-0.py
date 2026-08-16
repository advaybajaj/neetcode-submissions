class PrefixTree:

    def __init__(self):
        # empty pointer
        self.endOfWord = False
        self.children = dict()

    def insert(self, word: str) -> None:

        if not word:
            self.endOfWord = True
            return

        c = word[0]
        if c not in self.children:
            self.children[c] = PrefixTree()
        self.children[c].insert(word[1:])

    def search(self, word: str) -> bool:
        if not word:
            return self.endOfWord

        c = word[0]
        if c not in self.children:
            return False
        return self.children[c].search(word[1:])


    def startsWith(self, prefix: str) -> bool:

        if not prefix:
            return True
        
        c = prefix[0]
        if c not in self.children:
            return False

        return self.children[c].startsWith(prefix[1:])
        