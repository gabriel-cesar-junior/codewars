#https://www.codewars.com/kata/523a86aa4230ebb5420001e1/train/python
def anagrams(word,words):
    import re 
    from collections import OrderedDict, Counter
    result = []
    split_word = [i for i in word]
    r = re.compile('[a-zA-Z]')
    match = [r.findall(i) for i in words]
    for item in match:
        if Counter(split_word) == Counter(item):
            result.append(''.join(item))
    return result
print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])