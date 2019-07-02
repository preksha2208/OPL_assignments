# WRITE A TEST-SUITE OF A DOZEN J4 PROFRAM. (69L) 
class number:
   def __init__(self,a):
      self.a = a
   def interp(self):
       return self.a
class mult:
   def __init__(self, b, c):
      self.b = b
      self.c = c
   def interp(self):
      return self.b * self.c
   def __str__(self):   
       return ("("+"*"+" "+str(self.b)+" "+str(self.c)+ ")")  
class add:
   def __init__(self, d, e):
        self.d = d
        self.e = e 
   def interp(self):
      return self.d + self.e
   def __str__(self):
       return ("("+"+"+" "+str(self.d)+" "+str(self.e)+ ")")  
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
            string = " "
            for i in range(len(self.oper)):
                string = string + str(self.oper[i])
            
        return("(" +" " + string +" "+ ")")
class X :
    def __init__ (self,varnam):
        self.varnam = varnam
    def __str__(self):
        return(str(self.varnam[0]))
print(X(["var"]))
print(E(["perk"]))
print(E(["if","< 4 5",3,4]))
print(E(["<",3,4 ]))
print(V(7))
print(V(7.5))
print(V(True))
print(E(["if","> 4 5","true","false"]))
print(prim([">="]))
print(prim(["/"]))
print(prim(["<"]))
print(prim(["<=", 1, 2 ] ) )