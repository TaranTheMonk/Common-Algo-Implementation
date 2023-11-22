def bin_str_to_int(bin_str: str) -> int:
    """
    converting a string of binary to decimal 10 integer
    :param bin_str:
    :return:
    """
    return int(bin_str, 2)


def is_zero(bit_mask: int, n: int) -> bool:
    """
    check if a certain bit is 0, examples:
        1. 101 & 100 = 100
        2. 101 & 10 = 0
    :param bit_mask:
    :param n:
    :return:
    """
    return bit_mask & 1 << (n - 1) == 0


def is_one(bit_mask: int, n: int) -> bool:
    """
    check if a certain bit is 1, examples:
        1. 101 & 100 = 100
        2. 101 & 10 = 0
    :param bit_mask:
    :param n:
    :return:
    """
    return bit_mask & 1 << (n - 1) > 0


def set_to_zero(bit_mask: int, n: int) -> int:
    """
    to set a certain bit to 0, examples:
        1. 10101 ^ 100 = 10001
        2. 10101 ^ 1 = 10100
    :param bit_mask:
    :param n:
    :return:
    """
    # do xor if that bit is 1
    if bit_mask & 1 << (n - 1) > 0:
        return bit_mask ^ 1 << (n - 1)
    else:
        return bit_mask


def set_to_one(bit_mask: int, n: int) -> int:
    """
    to set a certain bit to 0, examples:
        1. 10101 | 100 = 10101
        2. 10101 | 10 = 10111
    :param bit_mask:
    :param n:
    :return:
    """
    return bit_mask | 1 << (n - 1)


def isolate_last_set(x: int) -> int:
    """
    to keep the bit from the last set, examples:
        1. 6 & (-6) -> 0000 0110 & 1111 1010 -> 10

    Note: negative value is represented via 2's complement in bits.
        6 -> 0000 0110 -reverse> 1111 1001 -add 1> 1111 1010 -> -6
    :param x:
    :return:
    """
    return x & (-x)
