class node:
    def __init__(self, data):
        self.data = data
        self.children = None
    
    def add_child(self, child):
        if self.children == None:
            self.children = []
        self.children.append(child)
        
    def is_leaf(self):
        return self.children == None

class scanner:
    # toks[i] must evaluate to the i-th token in the token stream.
    # Assumes toks does not change during parsing
    def __init__(self,toks):
        self._toks = toks
        self._i = 0
    
    # If no more tokens exist or current token isn't s, raise exception.
    # Otherwise pass over the current one and move to the next.
    def match(self,s):
        if (self._i < len(self._toks)) and (self._toks[self._i] == s):
            self._i += 1
        else:
            raise Exception
            
    # If any tokens remain return the current one. If no more, return None.
    def next(self):
        if self._i < len(self._toks):
            return self._toks[self._i]
        else:
            return None

def parseD(toks):
    tok = toks.next()
    rval = node('D')
    if (tok == 'a'):
        toks.match('a')
        rval.add_child(node('a'))
    elif tok == '(':
        toks.match('(')
        rval.add_child(node('('))
        rval.add_child(parseS(toks))
        toks.match(')')
        rval.add_child(node(')'))
    else:
        raise Exception
    return rval


def parseC(toks):
    tok = toks.next()
    rval = node('C')
    if tok in ('*', '/'):
        toks.match(tok)
        rval.add_child(node(tok))
        rval.add_child(parseD(toks))
        rval.add_child(parseC(toks))
    elif (tok in ('+', '-', ')', 'a') or tok == None):
        rval.add_child(node(''))
    else:
        raise Exception
    return rval


def parseB(toks):
    tok = toks.next()
    rval = node('B')
    if tok in ('a', '('):
        rval.add_child(parseD(toks))
        rval.add_child(parseC(toks))
    else:
        raise Exception
    return rval


def parseA(toks):
    tok = toks.next()
    rval = node('A')
    if tok in ('+', '-'):
        toks.match(tok)
        rval.add_child(node(tok))
        rval.add_child(parseB(toks))
        rval.add_child(parseA(toks))
    elif tok in ('a', ')') or (tok == None):
        rval.add_child(node(''))
    else:
        raise Exception
    return rval


def parseS(toks):
    tok = toks.next()
    return_value = node('S')
    if tok in ('a', '('):
        return_value.add_child(parseB(toks))
        
        

def parse(input):
    toks = scanner(input)
    rval = parseS(toks)
    if toks.next() != None:
        raise Exception
    return rval