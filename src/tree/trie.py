from typing import List, Optional


class TrieNode:
    def __init__(self):
        self.children: List[Optional["TrieNode"]] = [None] * 26
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self._ch_start_idx = ord("a")

    def _char_to_index(self, c: str):
        return ord(c) - self._ch_start_idx

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

    def search(self, key: str) -> bool:
        node = self.root
        for level in range(len(key)):
            index = self._char_to_index(key[level])

            if not node.children[index]:
                return False
            node = node.children[index]

        return node.is_end
