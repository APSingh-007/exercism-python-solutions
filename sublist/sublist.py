"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "B is Superlist"
SUPERLIST = "A is Superlist"
EQUAL = "A and B are Equal"
UNEQUAL = "A and B are Unequal"


def sublist(list_A, list_B):
    if list_A == list_B:
        return EQUAL
    if is_sublist(list_A, list_B):
        return SUPERLIST
    if is_sublist(list_B, list_A):
        return SUBLIST
    else:
        return UNEQUAL


def is_sublist(superlist, sublist):
    la, lb = len(superlist), len(sublist)
    if la < lb:
        return False
    for i in range(la - lb + 1):
        if superlist[i : i + lb] == sublist:
            return True
    return False
