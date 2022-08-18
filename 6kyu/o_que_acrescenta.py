#https://www.codewars.com/kata/53cce49fdf221844de0004bd/train/python
def addsup(a1, a2, a3):
    return [[x,y,x+y] for x in a1 for y in a2 if x+y in a3]
print(addsup([1,2,5],[3,1],[5,4,6]))