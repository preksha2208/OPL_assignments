#  ELIMINATE BIG-STEP INTERPRETER. (58L) 
class number:
   def __init__(self,a):
      self.a = a
class mult:
   def __init__(self, b, c):
      self.b = b
      self.c = c
   def __str__(self):   
       return ("("+"*"+" "+str(self.b)+" "+str(self.c)+ ")")  
class add:
   def __init__(self, d, e):
        self.d = d
        self.e = e 
   def __str__(self):
       return ("("+"+"+" "+str(self.d)+" "+str(self.e)+ ")")
class D :
    def __init__(self,lists):
        self.lists = lists
    def __str__(self):
        if len(self.lists) >= 4 and self.lists[0] == 'if' :
            return ("( " + str(self.lists[0]) +" " + str(self.lists[1]) + " " + str(self.lists[2]) + " " + str(self.lists[3]) + " " +  str(self.lists[4])+ " )")
        elif len(str(self.lists)) == 1:
            return(str(self.lists[0]))
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
class X :
    def __init__ (self,varnam):
        self.varnam = varnam
    def __str__(self):
        if len(self.var) == 1:
            return(str(self.lists[0]))
class F :
    def __init__(self,func):
        self.func = func
    def __str__(self):
        if len(self.func) == 1:
            return(str(self.func[0]))   
print(D(["if", prim(["<"]),"5 8",add(2,3), mult(4,2)]))