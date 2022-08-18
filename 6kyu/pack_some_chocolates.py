#https://www.codewars.com/kata/5f5daf1a209a64001183af9b/train/python
def make_chocolates(small, big, goal):
    a = small + big
    b = goal-big
    if (a*5 < goal):
        return -1
    smallNeeded = b * 5

    if smallNeeded <= 0:
        return 0
    return smallNeeded

           
print(make_chocolates(4, 1, 14))