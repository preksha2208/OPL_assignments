#CONVERT J0 TEST-SUITE INTO SEXPRS.(26L)
class sexpr: pass
class empty(sexpr):
    def __init__(self,empty_tuple):
      self.empty_tuple = empty_tuple
      empty_tuple = ()
    def mt(self):
      return self.empty_tuple
class cons(sexpr) :
    def __init__(self,const):
      self.const = const
    def __str__(self):
     return (str(self.const))
class strings(sexpr):
    def __init__(self,strng1):
      self.strng1 = strng1
    def strgs(self):
      return (self.strng1)
    def __str__(self):
     return ("("+str(self.strng1))
class pair(sexpr):
    def __init__(self,tup1):
      self.tup1 = tup1 
    def pairs(self):
      return (self.tup1)      
obj = empty(())
print(str(strings('*'))+" "+str(cons(3))+" "+str(strings('+'))+" "+str(cons(5))+" "+ str(obj.empty_tuple)+ ") )")