from typing import List


def binary_search(nums: List[int], val: int) -> bool:
    """
    search if val is in an ascending sorted list
    :param nums:
    :param val:
    :return:
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == val:
            return True
        elif nums[mid] < val:
            left = mid + 1
        else:
            right = mid - 1

    return False


def binary_search_less_or_equal(nums: List[int], val: int) -> int:
    """
    search the number of elements in an  ascending sorted list
    which are less or equal to val
    :param nums:
    :param val:
    :return:
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        # val is in the array
        if nums[mid] == val:
            # search till the last equals to val
            while mid + 1 < len(nums) and nums[mid + 1] == val:
                mid += 1
            return len(nums[: mid + 1])
        # mid is less than val, we ignore the left half
        elif nums[mid] < val:
            left = mid + 1
        # mid is greater than val, we ignore the right half
        else:
            right = mid - 1

    # val is not in the array, but nums[mid] is the most close one to val
    if nums[mid] < val:
        # search right till the last less than val
        while mid + 1 < len(nums) and nums[mid + 1] < val:
            mid += 1
        return len(nums[: mid + 1])
    else:
        # search left till the first less then val
        while mid - 1 > -1 and nums[mid - 1] > val:
            mid -= 1
        return len(nums[: mid])
