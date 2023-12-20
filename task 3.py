#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def sq_avg(*args):
    if args:
        sum_of_squares = sum(x**2 for x in args)
        return math.sqrt(sum_of_squares / len(args))
    else:
        return None


if __name__ == "__main__":
    print(sq_avg())
    print(sq_avg(3, 7, 1, 6, 9))
    print(sq_avg(1, 5, 8, 4, 3, 9, 6, 4))
