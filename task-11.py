#  INTERPRETER FOR J1 PROGRAM. (73L) 
class E :
    def __init__(self,lists):
        self.lists = lists
    def interp(self):
        if len(self.lists) == 4 and self.lists[0] == 'if' :
            if self.lists[2] > self.lists[3] :
                return (self.lists[2] + "is greater than" + self.lists[3])
            else :
                return (self.lists[3] + "is greater than" + self.lists[2])
        elif len(self.lists) >= 2:
            if self.lists[0] == '+':
                return (self.lists[1] + self.lists[2])
            elif self.lists[0] == '*' :
                return (self.lists[1] * self.lists[2])
            elif self.lists[0] == '/' :
                return (self.lists[1] / self.lists[2])
            elif self.lists[0] == '-' :
                return (self.lists[1] - self.lists[2])
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
    def interp(self):
         if len(self.oper) >= 2:
            if self.oper[0] == '+':
                return (self.oper[1] + self.oper[2])
            elif self.oper[0] == '*' :
                return (self.oper[1] * self.oper[2])
            elif self.oper[0] == '/' :
                return (self.oper[1] / self.oper[2])
            elif self.oper[0] == '-' :
                return (self.oper[1] - self.oper[2])
            elif self.oper[0] == '>' :
                return (self.oper[2] + "is greater than" + self.oper[3])
            elif self.oper[0] == '<' :
                return (self.oper[1] +"is less than" + self.oper[2])
            elif self.oper[0] == '>=' :
                return (self.oper[1] +" is greater than equal to" +self.oper[2])
            elif self.oper[0] == '<=' :
                return (self.oper[1] +"is less than equal to" +self.oper[2])
            elif self.oper[0] == '=' :
                return (self.oper[1] +" is equal to" +self.oper[2])
    def __str__(self):
        if len(self.oper) == 1:
            return(str(self.oper[0]))
        elif len(self.oper) >= 2:
            # print(self.oper)
            string = " "
            for i in range(len(self.oper)):
                string = string + str(self.oper[i])
        return("(" +" " + string +" "+ ")")
print(E(["if","< 5 7"," 5 ", " 7 "]))
print(E(["if","< 5 7"," 5 ", " 7 "]).interp())
print(E(["*",5,7]))
print(E(["*",5,7]).interp())
print(E(["+",5,7]))
print(E(["+",5,7]).interp())
print(prim(["/", 4, 2 ] ) )
print(prim(["/", 4, 2 ] ).interp() )