# -*- coding: utf-8 -*-
"""I've Been Everywhere, Man

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V6ooOqvClTd11H_m4EKZ5v_2geqFbzN-
"""

n = int(input())
for i in range(0, n):
    flight_set = {}
    f = int(input())
    for j in range(0, f):
        flight_set[input()] = 1
    print(len(flight_set))