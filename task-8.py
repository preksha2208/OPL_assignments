#  DEFINE DATA STRUCTURES TO REPRESENT J1 ALONG WITH PRETTY PRINTER. (32L) 
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
print(E(["perk"]))
print(E(["if","< 4 5",3,4]))
print(E(["<",3,4 ]))
print(prim([">="]))
print(prim(["<=", 1, 2 ] ) )