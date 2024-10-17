from functools import reduce
import math

def count_digits(num: int)->int:
    nnum = abs(int(num))
    nnum = str(nnum)
    length = len(nnum)
    return length

def all_less(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in enumerate(list1):
        if list1[i] > list2[i]:
            return False
    return True

def collapse(lst):
    collapsed_list = []
    i_1 = 0
    i_2 = 0
    for i in range(0, len(lst), 2):
        i_1 = lst[i]
        try:
            i_2 = lst[i+1]
        except IndexError:
            collapsed_list.append(i_1)
            return collapsed_list
        collapsed_list.append(i_1+i_2)
        length = len(collapsed_list)
        if length%2 != 0:
            collapsed_list.pop(length)
    return collapsed_list

def has_duplicate_value(mydict):
    if not dict and len(mydict) == 1:
        return False
    reversed_dict = {}
    for key, value in mydict.items():
        reversed_dict.setdefault(value, set()).add(key)
    duplicate = [ key for key, values in reversed_dict.items() if len(values) > 1 ]
    if duplicate:
        return True
    else:
        return False


def max_length(myset):
    if not myset:
        return None
    mylist = list(myset)
    for i in enumerate(mylist):
        if (len(mylist[0])) < len(mylist[i]):
            length = len(mylist[i])
    return length

def num_in_common(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    unique_num = 0
    for i in set1:
        if i in set2:
            unique_num+=1
    return unique_num

f = lambda f, l: "{0} , {1}".format(l, f)

f = lambda x, y: max(x, y)
f = lambda x, y: x if (x > y) else y

f = lambda x: x*x

def largest_even(lst):
    return max(x for x in lst if x % 2 == 0)

def total_circle_area(lst):
    if lst == []:
        return 0
    ret = list(map(lambda x: math.pi * x**2, lst))
    return reduce(lambda x, y: x + y, ret)

def glue_reverse(l):
    return ''.join(map(lambda x: x, reversed(l)))

lst_1 = ["the", "quick", "brown", "fox"]

lst_1 = glue_reverse(lst_1)
print(lst_1)
def abs_sum(lst1):
    return sum([abs(i) for i in lst1])

def count_negatives(l):
    return len(filter( lambda x: x < 0, l))

def count_vowels(s):
    return len(filter(lambda letter: letter in ['a', 'e' ,'i', 'o', 'u'], s.lower()))

def double_list(l):
    return map(lambda x: x + x, l)

words = ["four", "score", "and", "seven", "years", "ago"]

words2 = list(filter(lambda x: len(x) <=4 and len(x) >=3, words))

print(words2)