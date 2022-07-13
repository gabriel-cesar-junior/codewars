#https://www.codewars.com/kata/5ae840b8783bb4ef79000094/train/python

def merge(*dicts:dict):
    dicio = {}
    for i in dicts:
        for key, value in i.items():
            if key in dicio:
                dicio[key].append(value)
            else:
                dicio[key] = [value]
    return dicio
        
    
print(merge({"A": 1, "B": 2, "C": 3}, {"A": 4, "D": 5}))