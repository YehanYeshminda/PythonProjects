# Given an array of integers.
#
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.
#
# If the input is an empty array or is null, return an empty array.
#
# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

def count_numbers(array):
    if array == []:
        return []
    count_positive = sum(x > 0 for x in array)
    get_negative_sum = sum(x for x in array if x < 0)
    return [count_positive, get_negative_sum]


array_get = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
print(count_numbers(array_get))


# BEST SOLUTION
# def count_positives_sum_negatives(arr):
#     pos = sum(1 for x in arr if x > 0)
#     neg = sum(x for x in arr if x < 0)
#     return [pos, neg] if len(arr) else []