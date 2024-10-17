# class list135:

#     def __init__(self, first_item = None, rest_of_list = None):
#         self._first_item = first_item
#         self._rest_of_list = rest_of_list
                
#     def cons(self, first_item):
#         return list135(first_item, self)
    
#     def first(self):
#         return self._first_item
    
#     def rest(self):
#         return self._rest_of_list
    
#     def empty(self):
#         return self._rest_of_list == None
    
#     def len(self):
#         if(self.first() is None):
#             return 0
#         current = self.rest()
#         count = 0
#         while current is not None:
#             current = current.rest()
#             count +=1
#         return count

#     def __str__(self):
#         result = "["
#         cur = self
#         if cur.rest() != None:
#             result = result + str(cur._first_item)
#             cur = cur.rest()
#         while cur.rest() != None:
#             result = result + "," + str(cur._first_item)
#             cur = cur.rest()
#         return result + "]"

# # Rerverse using recursion

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

def _reverse(lst, acc):
    while lst.rest() is not None:
        acc = acc.cons(lst.first())
        lst = lst.rest()
    return acc



def reverse(lst:list135):
    acc = list135()
    return _reverse_rec(lst, acc)



# l = list135(0)
# l1 = l.cons(1)
# l2 = l1.cons(2)
# l3 = l2.cons(3)
# l4 = l3.cons(4)
# l5 = l4.cons(5)

# # print(l.rest)
# # print(l.first)

# print("Org: {}".format(l5))
# print("Reversed: {}".format(reverse(l5)))


def mult(a, b):
    if b == 0:
        return 0
    else:
        return a + mult(a, b-1)
    

ans = mult(2, 3)

print(ans)