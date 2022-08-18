#https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
from itertools import count


def move_zeros(lst):
    zeros = lst.count(0)
    while 0 in lst:
        lst.remove(0)
        lst.append(zeros*'0')
        return lst
print(move_zeros([1, 0, 1, 2, 0, 1, 3]))