# IMPLEMENT A DESUGAR FUNCTION THAT CONVERTS SEXPRS INTO J0.(44L) 
class desugar: pass
class mult(desugar):
   def __init__(self, b, c):
      self.b = b
      self.c = c
   def __str__(self):   
       return ("("+"*"+" "+str(self.b)+" "+str(self.c)+ ")")   
class add(desugar):
   def __init__(self, d, e):
        self.d = d
        self.e = e 
   def __str__(self):
       return ("("+"+"+" "+str(self.d)+" "+str(self.e)+ ")")    
object = mult(3,add(5,3)) 
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
    def __init__(self,strng1,strng2):
      self.strng1 = strng1
      self.strng2 = strng2
    def strgs(self):
      return (self.strng1)
    def __str__(self):
     return (str(self.strng1)+" " +str(self.strng2))
class pair(sexpr):
    def __init__(self,tup1):
      self.tup1 = tup1 
    def pairs(self):
      return (self.tup1)      
obj = empty(())    
obj1 = strings('(', strings("*",strings(cons(3),strings("(",strings("+", strings(cons(5),strings(cons(3),") )")))))))  
def desugarsj (obj1):
    print(object) 
desugarsj(object)