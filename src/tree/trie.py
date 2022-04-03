class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _char_to_index(self, c: str):
        return ord(ch) - ord('a')

    def insert(self, key: str):
        node = self.root
        for level in range(len(key)):
            index = self._char_to_index(key[level])

            # if current character is not present
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]

        # mark last node as leaf
        node.is_end = True

    def search(self, key):
        node = self.root
        for level in range(len(key)):
            index = self._char_to_index(key[level])

            if not node.children[index]:
                return False
            node = node.children[index]

        return node.is_end