from pyparsing import empty
class list135:
    def __init__(self, first_item = None, rest_of_list = None):
        self._first_item = first_item
        self._rest_of_list = rest_of_list

    def cons(self, first_item):
        return list135(first_item, self)

    def first(self):
        return self._first_item

    def len(self)->int:
        if(self.first() is None):
            return 0
        current = self.rest()
        count = 0
        while current is not None:
            current = current.rest()
            count +=1
        return count

    def __str__(self) -> str:
        current = self.rest()
        in_list = "(" + str(self.first())
        while current is not None:
            in_list += ', ' + str(current.first())
            current = current.rest()
        return in_list + ")"

    def rest(self):
        return self._rest_of_list
    
    def empty(self):
        return self._rest_of_list == None
    
# Rerverse using recursion

def _reverse_rec(lst_obj, acc):
    if lst_obj.rest() is None:
        return acc
    else:
        acc = acc.cons(lst_obj.first())
        return _reverse_rec(lst_obj.rest(), acc)

# 1 2 3 4 
# acc = 5
# lst_obj.rest = 1 2 3 4 

# Reverse using loops

# def _reverse(lst, acc):
#     while lst.rest() is not None:
#         acc = acc.cons(lst.first())
#         lst = lst.rest()
#     return acc



def reverse(lst:list135):
    acc = list135()
    return _reverse_rec(lst, acc)


v_01 = list135(2)
v_02 = v_01.cons(7)
v_03 = v_02.cons(6)
v_04 = v_03.cons(3)
v_05 = v_04.cons(1)
print(v_05)
print("Org: {}".format(v_05))
print("Reversed: {}".format(reverse(v_05)))
