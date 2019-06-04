#  WRITE A TEST-SUITE OF A DOZEN J1 PROGRAMS. (38L) 
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
             return ("(" + str(self.oper[0]) +" " + str(self.oper[1]) + " " + "(" + " " + str(self.oper[2]) + " " + str(self.oper[3]) + " " + str(self.oper[4]) + ")" + ")")   
print(E(["+"]))  
print(E(["if","< 4 5",3,4]))
print(E(["<",3,4 ]))
print(prim([">="]))
print(E(["if",">= a b","a is greater","b is greater"]))
print(E(["- 1"]))
print(prim( [ "/" ,25, "*",5,5]))
print(E(["if","== a str","its sexpr"," its not sexpr"]))
print(prim( [ "-" ,99, "/",9,3]))
print(V(5.7))
print(prim( [ "/" ,7.6, "*",5.2,3.4]))
print(prim([ "+" ,3, "/",21,3 ]) )