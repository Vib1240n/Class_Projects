import list135 as l


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

v_01 = l.list135(5)
v_02 = v_01.cons(7)
v_03 = v_02.cons(6)
v_04 = v_03.cons(3)
print(v_04.__str__)