#https://www.codewars.com/kata/52fb87703c1351ebd200081f/train/python

def what_century(year):
    sec = (int(year) + 99) // 100
    ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
    return ordinal(sec)
print(what_century("2011"))