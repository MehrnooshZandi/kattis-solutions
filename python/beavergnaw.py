# -*- coding: utf-8 -*-
"""Beavergnaw

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V6ooOqvClTd11H_m4EKZ5v_2geqFbzN-
"""

from math import pi

while True:
    line = input().split(' ')
    D, V = int(line[0]), int(line[1])

    if D == 0 and V == 0:
        break

    print(((((-6) * V) / pi) + (D * D * D)) ** (1 / 3))