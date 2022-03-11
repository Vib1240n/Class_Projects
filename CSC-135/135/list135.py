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
        # The tail end of the list
        current = self.rest()
        # [3] self.first returns head of list
        in_list = "(" + str(self.first())
        # Each while iteration effectively does
        while current is not None:
            # [6] : self.rest().first()
            in_list += ', ' + str(current.first())
            # [7] : self.rest().rest().first()
            # [5] : self.rest().rest().rest().first()
            current = current.rest()
            # [None] : self.rest().rest().rest().rest()
        return in_list + ")"

    def rest(self):
        return self._rest_of_list
    
    def empty(self):
        return self._rest_of_list == None


v_01 = list135(5)
v_02 = v_01.cons(7)
v_03 = v_02.cons(6)
v_04 = v_03.cons(3)
v_05 = v_04.cons(1)
print(v_01)
print(v_05)
print(v_05.len())
