# IMPLEMENT A SMALL-STEP INTERPRETER FOR J1 USING CONTEXTS. (48L)
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
class plug :
    def __init__ (self,temp_list):
        self.temp_list = temp_list
    def __str__(self):
        if(self.temp_list[1] == 'HOLE'):
            self.temp_list[1] = add(1,1)
            return ( "( if  (" + str(self.temp_list[0]) + " " + str(self.temp_list[1])  +" "+ str(self.temp_list[2]) + " )" + " " +str(self.temp_list[3]) +" " + str(self.temp_list[4]) + " )"   )
        elif (self.temp_list[2] == 'HOLE'):
            self.temp_list[2] = add(1,1)
            return ( "( if  (" + str(self.temp_list[0]) + " " + str(self.temp_list[1])  +" "+ str(self.temp_list[2]) + " )" + " " +str(self.temp_list[3]) +" " + str(self.temp_list[4]) + " )"   )
        elif (self.temp_list[3] == 'HOLE'):
            self.temp_list[3] = add(1,1)
            return ( "( if  (" + str(self.temp_list[0]) + " " + str(self.temp_list[1])  +" "+ str(self.temp_list[2]) + " )" + " "+str(self.temp_list[3]) +" " + str(self.temp_list[4]) + " )"   )
    def interp(self):
        if(self.temp_list[1] == 'HOLE'):
            self.temp_list[1] = add(1,1)
            if (self.temp_list[0] == '<'):
                return(str(self.temp_list[3]))
            elif (self.temp_list[0] == '>'):
                return(str(self.temp_list[4]))
        elif (self.temp_list[2] == 'HOLE'):
            self.temp_list[2] = add(1,1)
            if (self.temp_list[0] == '<'):
                return(str(self.temp_list[4]))
            elif (self.temp_list[0] == '>'):
                return(str(self.temp_list[3]))
        elif (self.temp_list[3] == 'HOLE'):
            self.temp_list[3] = add(1,1)
            if (self.temp_list[0] == '<'):
                return(str(self.temp_list[3]))
            elif (self.temp_list[0] == '>'):
                return(str(self.temp_list[4])) 
print(plug(["<","HOLE",5,"5 is greater","2 is greater"]))
print(plug(["<","HOLE",5,"5 is greater","2 is greater"]).interp())
print(plug([">",5,"HOLE",3,4]))
print(plug([">",5,"HOLE",3,4]).interp())