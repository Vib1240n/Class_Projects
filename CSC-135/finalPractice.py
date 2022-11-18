# #3) Write a function count_true in Scheme or Racket that takes a one-input boolean function f and a list xs as inputs, and returns how many of the inputs cause f to evaluate to true. For example (count_true odd? ’(1 2 3)) would evaluate to 2.

class list135:

    def __init__(self, first_item = None, rest_of_list = None):
        self._first_item = first_item
        self._rest_of_list = rest_of_list
                
    def cons(self, first_item):
        return list135(first_item, self)
    
    def first(self):
        return self._first_item
    
    def rest(self):
        return self._rest_of_list
    
    def empty(self):
        return self._rest_of_list == None
    
    def len(self):
        if(self.first() is None):
            return 0
        current = self.rest()
        count = 0
        while current is not None:
            current = current.rest()
            count +=1
        return count

    def __str__(self):
        result = "["
        cur = self
        if cur.rest() != None:
            result = result + str(cur._first_item)
            cur = cur.rest()
        while cur.rest() != None:
            result = result + "," + str(cur._first_item)
            cur = cur.rest()
        return result + "]"


def count_true(func, lst: list135, acc):
    if lst.is_empty():
        return 0
    elif func(lst.first()):
        return 1 + count_true(func, lst.rest())
    else:
        return count_true(func, lst.rest())
            

        
    
    
    
if __name__ == '__main__':
    l = list135(0)
    l1 = l.cons(1)
    l2 = l1.cons(2)
    l3 = l2.cons(3)
    l4 = l3.cons(4)
    l5 = l4.cons(5)
    
    num = count_true(count_true, l)
    print(num)