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
    
    def len(self)->int:
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

def _reverse(self, l:list135, acc = None):
        current = l
        if acc is None:
            acc = list135()
        while current is not None:
            return(l.rest())
        if current.rest() is None:
            new_curr = current
            acc.cons(new_curr.first())
        return _reverse(acc)


def reverse(self, l:list135):
    return _reverse(list135)



l = list135()
l2 = l.cons(1)
l3 = l2.cons(2)
l4 = l3.cons(3)
l5 = l4.cons(4)
l6 = l5.cons(5)


print("l: {}".format(l))
print("l  first: {}".format(l.first()))
print("l2 first: {}".format(l2.first()))
print("l2 rest: {}".format(l2.rest()))
print("l6: {}".format(l6))
print("l6 first: {}".format(l6.first()))