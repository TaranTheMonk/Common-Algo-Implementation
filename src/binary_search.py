class Solution:
    def max_value(self, n: int, index: int, max_sum: int) -> int:
        """
        lower bound: maxSum / n
        """
        num_before = index
        num_after = n - 1 - index

        # index value is in [1, maxSum]
        l, r = 1, max_sum
        while l <= r:
            x = (l + r) // 2

            # sum before index
            if num_before > 0:
                before_sum = ((x - 1) + (x - num_before)) * num_before / 2
            else:
                before_sum = 0

            # sum after index
            if num_after > 0:
                after_sum = ((x - 1) + (x - num_after)) * num_after / 2
            else:
                after_sum = 0

            # update boundary
            if before_sum + x + after_sum < max_sum:
                l = x + 1
            elif before_sum + x + after_sum > max_sum:
                r = x - 1
            else:
                break

        return x
