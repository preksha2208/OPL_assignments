#  DEFINE DATA STRUCTURES TO REPRESENT SEXPRS. (13L) 
class sexpr: pass
class empty(sexpr):
    def __init__(self,empty_tuple):
      self.empty_tuple = empty_tuple
class cons(sexpr) :
    def __init__(self,const):
      self.const = const
class strings(sexpr):
    def __init__(self,strng1):
      self.strng1 = strng1
class pair(sexpr):
    def __init__(self,tup1):
      self.tup1 = tup1 