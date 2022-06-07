# All Star Code Challenge #18
#
# Create a function that accepts 2 string arguments and returns an integer of the count of occurrences the 2nd argument is found in the first one.
#
# If no occurrences can be found, a count of 0 should be returned.
#
# ("Hello", "o")  ==>  1
# ("Hello", "l")  ==>  2
# ("", "z")       ==>  0

def count_same_occurance(string, letter):
    # ACTUAL TEST MODEL IMPLEMENTED
    list1 = len([x for x in list(string) if x == letter])
    return list1

    # TEST MODEL
    # count = 0
    # for i in range(len(list(string))):
    #     if string[i].lower() == letter:
    #         count += 1
    # return count

print(count_same_occurance("Hello", "l"))

# KATA SOLUTION
# def strCount(string, letter):
#     return string.count(letter)