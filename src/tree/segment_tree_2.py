from typing import List, Tuple


class SegmentTree:
    def __init__(self, nums: List[int], k: int):
        """
        Each node stores:
            1. segment product % k.
            2. number of prefix arrays in the segment, with product = x (mod k)

        For Leetcode-3525-Find X Value of Array II.
        """
        self._n = len(nums)
        self._k = k

        # Tree size is ~4n, each stores (prod % k, count_array)
        self._tree: list = [None for _ in range(4 * self._n)]

        # Build the tree
        self._build(0, 0, self._n - 1, nums)

    def _build(self, node: int, left: int, right: int, nums: List[int]):
        """
        Build a node.
        """
        # when left == right, it's a leaf node
        if left == right:
            self._tree[node] = (0, [0] * self._k)

            rem = nums[left] % self._k
            self._tree[node][0] = rem
            self._tree[node][1][rem % self._k] = 1
        # otherwise, build child first
        else:
            self._tree[node] = (0, [0] * self._k)

            # child nodes
            child_node_l = 2 * node + 1
            child_node_r = 2 * node + 2

            # build child nodes
            mid = (left + right) // 2
            self._build(child_node_l, left, mid, nums)
            self._build(child_node_r, mid, right, nums)

            # build this node
            self._tree[node] = self._merge(child_node_l, child_node_r)

    def _merge(self, left_node: int, right_node: int) -> Tuple[int, list]:
        """
        Merge the values of two child node.
        """
        left_rem, left_cnt = self._tree[left_node]
        right_rem, right_cnt = self._tree[left_node]

        rem = (left_rem * right_rem) % self._k

        cnt = left_cnt.copy()


    def query(self):
        pass

    def _query(self):
        pass

    def update(self):
        pass
