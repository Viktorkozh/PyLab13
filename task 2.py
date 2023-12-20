#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def harm_avg(*args):
    if args:
        return len(args) / sum(1 / x for x in args)
    else:
        return None


if __name__ == "__main__":
    print(harm_avg())
    print(harm_avg(3, 7, 1, 6, 9))
    print(harm_avg(1, 5, 8, 4, 3, 9, 6, 4))
