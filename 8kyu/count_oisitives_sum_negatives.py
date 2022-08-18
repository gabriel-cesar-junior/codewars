def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []
    positives = sum([1 for i in arr if i >0])
    negatives = sum([i for i in arr if i <0])
    return[positives,negatives]
print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))