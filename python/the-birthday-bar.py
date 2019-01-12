#!/bin/python3

import itertools
import collections


def sliding_window(n, seq):
    """
    Copied from toolz
    https://toolz.readthedocs.io/en/latest/_modules/toolz/itertoolz.html#sliding_window

    A sequence of overlapping subsequences

    >>> list(sliding_window(2, [1, 2, 3, 4]))
    [(1, 2), (2, 3), (3, 4)]

    This function creates a sliding window suitable for transformations like
    sliding means / smoothing

    >>> mean = lambda seq: float(sum(seq)) / len(seq)
    >>> list(map(mean, sliding_window(2, [1, 2, 3, 4])))
    [1.5, 2.5, 3.5]
    """
    return zip(*(collections.deque(itertools.islice(it, i), 0) or it
                 for i, it in enumerate(itertools.tee(seq, n))))


def birthday_chocolate(squares, day, month):
    consecutive_sums = map(lambda piece: sum(piece),
                           sliding_window(month, squares))
    birthday_bars = list(filter(lambda consecutive_sum: day == consecutive_sum,
                                consecutive_sums))
    return len(birthday_bars)


_ = int(input().strip())
SQUARES = list(map(int, input().strip().split(' ')))
DAY, MONTH = map(int, input().strip().split(' '))
print(birthday_chocolate(SQUARES, DAY, MONTH))
