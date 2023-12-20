#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def geom_avg(*args):
    if args:
        prod = math.prod(args)
        return prod**(1/len(args))
    else:
        return None


if __name__ == "__main__":
    print(geom_avg())
    print(geom_avg(3, 7, 1, 6, 9))
    print(geom_avg(1, 5, 8, 4, 3, 9, 6, 4))
