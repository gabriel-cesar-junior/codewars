#https://www.codewars.com/kata/51b6249c4612257ac0000005/train/python

def solution(roman):
    roman_num = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }

    acum = 0
    for indice in range(len(roman)):
        num_atual = roman_num[roman[indice]]
        num_ant = roman_num[roman[indice-1]]
        if indice == 0 or num_ant >= num_atual:
            acum += num_atual    
        else:
            acum += num_atual - num_ant*2
    return acum
    

print(solution('MMMCMXLIX'))