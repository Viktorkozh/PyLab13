#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sum_after_zero(*args):
    if args:
        values = [float(arg) for arg in args]
        i_zero = 0

        for i, item in enumerate(values):
            if item == 0:
                i_zero = i

        if i_zero == 0:
            return "No zeros"

        a_cut = values[i_zero + 1:]
        return sum([item for item in a_cut])
    else:
        return None


if __name__ == "__main__":
    print(sum_after_zero())
    print(sum_after_zero(3, 7, 1, 6, 9))
    print(sum_after_zero(1, 5, 8, 9, 0, 5, 8, 9, 4, 3))
