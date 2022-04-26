import math
from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Node:
    left_idx: int
    right_idx: int
    size: int
    max_size: int
    prefix_size: int
    suffix_size: int


class SegmentTree:
    """
    Segment tree is a logarithmic data structure that operates on a fixed-size array.
    Leaves of the segment tree are elements of the array, and non-leaf nodes hold
    some value of interest (sum, average, etc.) for the underlying segments.

    Segment tree can be implemented using an array of 2 ** (ceil(log_2(n)) + 1) - 1 size.
    You will need to know the index of the current node (root's index is zero),
    and left and right positions of the current segment.

    The left child index is i * 2 + 1, and the right child index is i * 2 + 2.
    We also adjust left and right positions for the children.

    When left and right are equal - we've reached the leaf node.

    This implementation is for Leetcode-2213-Longest Substring of One Repeating Character
    """

    def __init__(self, s: str):
        self._s = list(s)

        # leaf nodes are all elements
        # so in total 2 ** (ceil(log_2(n)) + 1) - 1 nodes
        # why ?
        # for a full binary tree with n leaf nodes, it has 2 ** (log_2(n) + 1) - 1 nodes in together
        self._tree: List[Optional[Node]] = [None] * (
            2 ** (math.ceil(math.log(len(self._s), 2)) + 1) - 1
        )
        self._init_tree(0, 0, len(self._s) - 1)

    def _init_tree(self, tree_idx: int, left_arr_idx: int, right_arr_idx: int):
        """
        init a tree rooted on tree_idx for array[left_arr_idx:right_arr_idx + 1]
        :return:
        """
        # the leaf node contains the element
        if left_arr_idx == right_arr_idx:
            self._tree[tree_idx] = Node(
                left_idx=left_arr_idx,
                right_idx=right_arr_idx,
                size=1,
                max_size=1,
                prefix_size=1,
                suffix_size=1,
            )
        else:
            mid = (left_arr_idx + right_arr_idx) // 2
            self._init_tree(tree_idx * 2 + 1, left_arr_idx, mid)
            self._init_tree(tree_idx * 2 + 2, mid + 1, right_arr_idx)
            self._update_node(
                tree_idx
            )

    def _update_tree(self, tree_idx: int, array_idx: int):
        """
        Update the tree rooted on tree_idx.
        Array_idx is where the array is updated.
        :param tree_idx:
        :param array_idx:
        :return:
        """
        node = self._tree[tree_idx]
        # reach non-leaf node
        if node.left_idx != node.right_idx:
            mid = (node.left_idx + node.right_idx) // 2
            # in left child
            if array_idx <= mid:
                self._update_tree(tree_idx * 2 + 1, array_idx)
            # in right child
            else:
                self._update_tree(tree_idx * 2 + 2, array_idx)

            self._update_node(
                tree_idx
            )

    def _update_node(self, node_idx: int):
        left_child, right_child = self._tree[2 * node_idx + 1], self._tree[2 * node_idx + 2]

        max_size = max(left_child.max_size, right_child.max_size)
        prefix_size = left_child.prefix_size
        suffix_size = right_child.suffix_size

        # the suffix from left + prefix from right can form a longer one
        if self._s[left_child.right_idx] == self._s[right_child.left_idx]:
            max_size = max(max_size, left_child.suffix_size + right_child.prefix_size)

            # prefix can be merged if:
            # 1. both has the same left-most char
            # 2. left child's prefix ends in the right-most char
            if left_child.prefix_size == left_child.size:
                prefix_size += right_child.prefix_size

            # suffix can be merged if:
            # 1. both has the same right-most char
            # 2. right child's suffix starts in the left-most char
            if right_child.suffix_size == right_child.size:
                suffix_size += left_child.suffix_size

        if self._tree[node_idx] is None:
            self._tree[node_idx] = Node(
                left_idx=left_child.left_idx,
                right_idx=right_child.right_idx,
                size=left_child.size + right_child.size,
                max_size=max_size,
                prefix_size=prefix_size,
                suffix_size=suffix_size,
            )
        else:
            self._tree[node_idx].left_idx = left_child.left_idx
            self._tree[node_idx].right_idx = right_child.right_idx
            self._tree[node_idx].size = left_child.size + right_child.size
            self._tree[node_idx].max_size = max_size
            self._tree[node_idx].prefix_size = prefix_size
            self._tree[node_idx].suffix_size = suffix_size

    def update(self, idx: int, c: str):
        """
        update the array[idx] with c, also updates the tree.
        :param idx:
        :param c:
        :return:
        """
        if self._s[idx] != c:
            self._s[idx] = c
            self._update_tree(0, idx)

    def query(self):
        return self._tree[0].max_size
