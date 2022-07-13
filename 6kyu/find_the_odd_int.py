#https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python

def find_it(seq):
    for num in seq:
        def countX(seq, num): 
            return seq.count(num)
        if (countX(seq,num)%2) != 0:
            return num
            
        
print(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]))