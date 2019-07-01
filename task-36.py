#  Extend desugar to support let expressions.(70L) 
class E :
    def __init__(self,lists):
        self.lists = lists
    def __str__(self):
        if len(self.lists) == 1:
            return(str(self.lists[0]))
        if len(self.lists) == 4 and self.lists[0] == 'if' :
            return (str(self.lists[0]) +" " + "(" + " " + str(self.lists[1]) + " " + ")" + " " + str(self.lists[2]) + " " + str(self.lists[3]))
        elif len(self.lists) >= 2:
            return("(" + " " + str(self.lists[0]) + " " +  str(self.lists[1]) + " " + str(self.lists[2])+ " " + ")")
class V:
    def __init__(self,val):
      self.val = val
    def __str__ (self):
        if isinstance(self.val,(int,float,bool)) :
            return(str(self.val))
        if isinstance(self.val,str) :
            return(str(self.val))
class prim:
    def __init__(self,oper):
      self.oper = oper
    def __str__(self):
        if len(self.oper) == 1:
            return(str(self.oper[0]))
        elif len(self.oper) >= 2:
            # print(self.oper)
            string = " "
            for i in range(len(self.oper)):
                string = string + str(self.oper[i])
            
        return("(" +" " + string +" "+ ")")
object = E(["if","< a b"," b is greater"," a is greater"])
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
obj1 = strings('if', strings("(",strings("< a b",strings(")",strings("b is greater", "a is greater")))))  
def desugarsj (obj1):
    print(object) 
desugarsj(object)
class let:
    def __init__(self,letlist):
        self.letlist = letlist
    def __str__(self):
        return("desugar of let( [" + str(self.letlist[0]) + " " + str(self.letlist[2]) + " ] [ " + str(self.letlist[1]) + " " + str(self.letlist[3]) + " ] ) is:" )
    def desugarlet(self):
        return("( \u03BB [" + str(self.letlist[0]) + " " + str(self.letlist[1]) + " ] " + str(self.letlist[2]) + " " + str(self.letlist[3]) + " )" )
print(let(["x","y",5,7]))
print(let(["x","y",5,7]).desugarlet())