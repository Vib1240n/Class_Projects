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

# production
# S' → S$
# S → BA
# A → +BA | -BA | λ
# B → DC
# C → *DC | /DC | λ
# D → a | (S) 

def parse(input):
    toks = scanner(input)
    stack = ['S']
    while len(stack) > 0:
        top = stack.pop()      
        tok = toks.next()  
        if top in ('+', '-', '*','/','a','(',')'):     
            toks.match(top)
        elif top == "S" and (tok == 'a' or tok == '('):  
            stack.append('A')            
            stack.append('B')
        elif top == 'A' and (tok == '+' or tok == '-'):  
            stack.append('A')            
            stack.append('B')
            if tok == '+':
                stack.append('+')
            else:
                stack.append('-')
        elif top == 'A' and (tok == ')' or tok == None):
            pass
        elif top == 'B' and (tok == 'a' or tok == '('):
            stack.append('C')
            stack.append('D')
        elif top == 'C' and (tok == '*' or tok == '/'):
            stack.append('C')
            stack.append('D')
            if tok == '*':
                stack.append('*')
            else:
                stack.append('/')
        elif top == 'C' and (tok == '+' or tok == '-' or tok == ')' or tok == None):
            pass
        elif top == 'D' and tok == 'a':
            stack.append('a')
        elif top == 'D' and tok == '(':
            stack.append(')')
            stack.append('S')
            stack.append('(')
        else:
            raise Exception    
    if toks.next() != None:
        raise Exception



# test cases
try:
    # THE CORRECT OUTPUT OF THE TEST CASE
    parse ("j")
    parse ("(a)")
    parse ("((a))")
    parse ("a+a")
    parse ("a*a")
    parse ("((a)/(a)-(a))")
    parse ("((a)/(a)-(a))*((a)/(a)-(a))")
    parse ("a+a*a-a/a")
    parse ("a/a-a*a+a")
    parse ("(a+a*a-a/a)")
    parse ("(a/a-a*a+a)")
    parse ("(a+(a*a*a)+a+a)")
    parse ("(a*(a+a+a)*a*a)")
except:
    print("Reject")
else:
    print("Accept")