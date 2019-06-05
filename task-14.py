# IMPLEMENT FIND-REDEX, A FUNCTION THAT BREAKS A TERM INTO A CONTEXT AND A REDEX.(26L) 
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
def redex(temp_list):
    if(str(temp_list[1]) == str(add(1,1))):
        temp_list[1] = "HOLE"
        return ( "( if  (" + str(temp_list[0]) + str(temp_list[1])  +" "+ str(temp_list[2]) + " )" + str(temp_list[3]) +" " + str(temp_list[4]) + " )"   )
    elif (str(temp_list[2]) == str(add(1,1))):
        temp_list[2] = "HOLE"
        return ( "( if  (" + str(temp_list[0]) + str(temp_list[1])  +" "+ str(temp_list[2]) + " )" + str(temp_list[3]) +" " + str(temp_list[4]) + " )"   )
    elif (str(temp_list[3]) == str(add(1,1))):
        temp_list[3] = "HOLE"
        return ( "( if  (" + str(temp_list[0]) + str(temp_list[1])  +" "+ str(temp_list[2]) + " )" + str(temp_list[3]) +" " + str(temp_list[4]) + " )"   )
print(redex(["< ",add(1,1),5,3,4]))
print(add(1,1))
print(redex(["< ",5,add(1,1),3,4]))
print(add(1,1))