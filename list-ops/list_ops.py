def append(list1, list2):
    return list1 + list2


def concat(lists):
    result = []
    for item in lists:
        result += item
    return result


def filter(function, list):
    result = []
    for item in list:
        if function(item):
            result += [item]
    return result


def length(list):
    len = 0
    len = sum(1 for x in list)
    return len


def map(function, list):
    for i, item in enumerate(list):
        list[i] = function(item)
    return list


def foldl(function, list, initial):
    for item in list:
        initial = function(initial, item)
    return initial


def foldr(function, list, initial):
    for item in reversed(list):
        initial = function(initial, item)
    return initial


def reverse(list):
    return list[::-1]
