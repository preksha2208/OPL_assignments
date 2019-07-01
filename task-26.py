#  Define a substitution function that plugs the value of a variable into references to that variable.(34L) 
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
class E :
    def __init__(self,lists):
        self.lists = lists
    def __str__(self):
        if len(self.lists) == 4 and self.lists[0] == 'if' :
            return ("( " + str(self.lists[0]) +" " + str(self.lists[1]) + " " + str(self.lists[2]) + " " + str(self.lists[3]) + " )")
        if len(self.lists) == 1:
            return(str(self.lists[0]))
        elif len(self.lists) >= 2:
            return("(" + " " + str(self.lists[0]) + " " +  str(self.lists[1]) + " " + str(self.lists[2])+ " " + ")")
def plug(temp_list):
    if(temp_list[1] == 'e'):
        temp_list[1] = add(1,1)
        return ( "( " + str(temp_list[0]) + " " + str(temp_list[1]) + " " + str(temp_list[2]) + " " + str(temp_list[3]) +" )"   )
    elif (temp_list[2] == 'e'):
        temp_list[2] = add(1,1)
        return ( "( " + str(temp_list[0]) + " " + str(temp_list[1]) + " " + str(temp_list[2]) + " " + str(temp_list[3]) +" )"   )    
    elif (temp_list[3] == 'e'):
        temp_list[3] = add(1,1)
        return ( "( " + str(temp_list[0]) + " " + str(temp_list[1]) + " " + str(temp_list[2]) + " " + str(temp_list[3]) +" )"   )
print(E(["if","e",2,5]))
print(plug(["if ","e",2,5]))