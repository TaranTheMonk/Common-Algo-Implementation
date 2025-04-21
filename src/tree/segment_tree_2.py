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
        Build the tree.
        """
        # when left == right, it's a leaf node
        if left == right:
            self._tree[node] = [0, [0] * self._k]

            rem = nums[left] % self._k
            self._tree[node][0] = rem
            self._tree[node][1][rem % self._k] = 1
        # otherwise, build child first
        else:
            self._tree[node] = [0, [0] * self._k]

            # child nodes
            child_node_l = 2 * node + 1
            child_node_r = 2 * node + 2

            # build child nodes
            mid = (left + right) // 2
            self._build(child_node_l, left, mid, nums)
            self._build(child_node_r, mid + 1, right, nums)

            # build this node
            self._tree[node] = self._merge(
                self._tree[child_node_l], self._tree[child_node_r]
            )

    def _merge(
        self, left_value: Tuple[int, list], right_value: Tuple[int, list]
    ) -> Tuple[int, list]:
        """
        Merge two values.
        """
        left_rem, left_cnt = left_value
        right_rem, right_cnt = right_value

        rem = (left_rem * right_rem) % self._k

        # for any prefix arrays in right with remainder r,
        # if we can form left_rem * r % k = x, we can concat it with the whole left segment.
        cnt = left_cnt.copy()
        for r in range(self._k):
            cnt[(left_rem * r) % self._k] += right_cnt[r]

        return rem, cnt

    def _update(self, node: int, left: int, right: int, idx: int, val: int):
        if left == right:
            self._tree[node] = [0, [0] * self._k]

            rem = val % self._k
            self._tree[node][0] = rem
            self._tree[node][1][rem % self._k] = 1
        else:
            mid = (left + right) // 2

            child_node_l = 2 * node + 1
            child_node_r = 2 * node + 2
            if idx <= mid:
                self._update(2 * node + 1, left, mid, idx, val)
            else:
                self._update(2 * node + 2, mid + 1, right, idx, val)

            self._tree[node] = self._merge(
                self._tree[child_node_l], self._tree[child_node_r]
            )

    def update(self, idx: int, val: int):
        self._update(0, 0, self._n - 1, idx, val)

    def _query(
        self, node: int, left: int, right: int, from_idx: int, to_idx: int
    ) -> Tuple[int, list]:
        # out of range
        if from_idx > right or to_idx < left:
            return 1, [0] * self._k

        # fully in the range
        if from_idx <= left and to_idx >= right:
            return self._tree[node]

        # partially in the range
        mid = (left + right) // 2
        left_value = self._query(2 * node + 1, left, mid, from_idx, to_idx)
        right_value = self._query(2 * node + 2, mid + 1, right, from_idx, to_idx)

        return self._merge(left_value, right_value)

    def query(self, idx: int, x: int):
        return self._query(0, 0, self._n - 1, idx, self._n - 1)[1][x]


class Solution:
    def resultArray(
        self, nums: List[int], k: int, queries: List[List[int]]
    ) -> List[int]:
        """
        Observations:
            1. Normal array:
                1.1. Update, O(1).
                1.2. Range operation, O(n).
            2. Segment tree:
                2.1. Update, O(log n).
                2.2. Range operation, O(log n).
                2.3. Only works for fixed size array.
        """
        st = SegmentTree(nums, k)

        ret = list()
        for idx, val, start, x in queries:
            st.update(idx, val)
            ret.append(st.query(start, x))

        return ret


if __name__ == "__main__":
    print(Solution().resultArray(nums=[1, 1, 2, 1, 1], k=2, queries=[[2, 1, 0, 1]]))
