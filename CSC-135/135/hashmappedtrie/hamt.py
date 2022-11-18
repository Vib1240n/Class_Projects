# Hash Array Mapped Trie - Used in CSC 135, Sacramento State
# Written by Ted Krovetz, February 2022
# 
# This implementation assumes that the objects pointed at by the key and value
# references stored in the HAMT structure do not change during the lifetime
# of the structure.
class hamt:

    DEG = 4      # Children per node (must be power of 2)
    BITS = 2     # log2(DEG), bits needed to select child
    MASK = 0b11  # Bitmask for extracting low BITS bits (DEG - 1) 3?

    def __init__(self, key, value, children=None):
        self._key = key
        self._value = value
        if children == None:
            self._children = [None] * hamt.DEG
        else:
            self._children = children

    def _set(self, key, value, hashbits):
        
        # Each node encountered during search will get altered.
        # To maintain persistence, each is duplicated, updated, returned.
        if (self._key == key):
            # This node matches key. Return duplicate with new value
            return hamt(self._key, value, self._children)
        else:
            # Continue search using hashbits to pick direction
            child_num = hashbits & hamt.MASK
            # Copy can reuse key/value. Child list gets updated, so duplicate
            copy = hamt(self._key, self._value, list(self._children))
            if (copy._children[child_num] == None):
                # End of search, key not found, add new node
                copy._children[child_num] = hamt(key, value)
            else:
                # Continue by asking appropriae child to set key/value
                copy._children[child_num] = copy._children[child_num].     \
                                    _set(key, value, hashbits >> hamt.BITS)
            return copy

    def set(self, key, value):
        # Pass key/value and hashbits to recursive helper
        return self._set(key, value, hash(key))
    
    def _get(self, key, hashbits):
        child = hashbits & hamt.MASK
        if self._key == key:
            return self._value
        elif self._children[child] != None:
            return self._children[child]._get(key, hashbits>>hamt.BITS)
        else:
            return None 

    def get(self, value):
        return self._get(value, hash(value))


    def len(self):
        counter = 1
        for i in range(hamt.DEG):
            if(self._children[i] is not None):
                counter += self._children[i].len()
        return counter
    
    def map(self, f):
        copy = hamt(self._key, self._value, list(self._children))
        for i in range(hamt.DEG):
            if(copy._children[i] is not None):
                copy._children[i] = copy._children[i].map(f)
        copy._value = f(copy._key, copy._value)                         #f = lambda x,y: x+y
        return copy

    def __str__(self):
        s = "[({},{})".format(str(self._key),str(self._value))
        for i in range(hamt.DEG):
            if (self._children[i] == None):
                s = s + "x"
            else:
                s = s + str(self._children[i])
        return s + "]"



a =  hamt("A", "a")
b = a.set("B", "b")
c = b.set("C", "c")
d = c.set("D", "d")
e = d.set("E", "e")
f = e.set("F", "f")
g = f.set("G", "g")
h = g.set("H", "h")
i = h.set("I", "i")
j = i.set("J", "j")
k = j.set("K", "k")

print("{} - {}".format(a, a.len()))
print("{} - {}".format(d, d.len()))
print("{} - {}".format(e, e.len()))
print("{} - {}".format(f, f.len()))
print("{} - {}".format(g, g.len()))
print("{} - {}".format(h, h.len()))
print("{} - {}".format(i, i.len()))
print("{} - {}".format(j, j.len()))
print("{} - {}".format(k, k.len()))
print("map" + str(k.map(lambda x,y: x + y)))
print("eol")