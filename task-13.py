# IMPLEMENT PLUG, A FUNCTION THAT FILLS THE HOLE IN A CONTEXT WITH A PROGRAM.(38L) 
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
class types :
    def __init__(self,list1):
        self.list1 = list1
    def __str__(self):
        if self.list1[1] == 'C':
            return(" the context format is type-1")
        elif self.list1[2] == 'C':
            return(" the context format is type-2")
        elif self.list1[3] == 'C':
            return(" the context format is type-3")
def plug(temp_list):
    if(temp_list[1] == 'HOLE'):
        temp_list[1] = add(1,1)
        return ( "( if  (" + str(temp_list[0]) + str(temp_list[1])  +" "+ str(temp_list[2]) + " )" + str(temp_list[3]) +" " + str(temp_list[4]) + " )"   )
    elif (temp_list[2] == 'HOLE'):
        temp_list[2] = add(1,1)
        return ( "( if  (" + str(temp_list[0]) + str(temp_list[1])  +" "+ str(temp_list[2]) + " )" + str(temp_list[3]) +" " + str(temp_list[4]) + " )"   )
    elif (temp_list[3] == 'HOLE'):
        temp_list[3] = add(1,1)
        return ( "( if  (" + str(temp_list[0]) + str(temp_list[1])  +" "+ str(temp_list[2]) + " )" + str(temp_list[3]) +" " + str(temp_list[4]) + " )"   )
temp_type = types(["if < ","C",5,3,4])
print(temp_type)
print(plug(["< ","HOLE",5,3,4]))
temp_type = types(["if < ",5,"C",3,4])
print(temp_type)
print(plug(["< ",5,"HOLE",3,4]))