# REFINE FIND-REDEX SO THAT IT LOOKS FOR EVALATION CONTEXTS. (37L) 
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

class redex:
    def __init__(self,temp_list):
        self.temp_list = temp_list
    def __str__(self):
        if(str(self.temp_list[0]) == str(add(1,1))):
            self.temp_list[0] = "E"
            return ( "( if  (" + " " +str(self.temp_list[0]) + " )" + " " +str(self.temp_list[3]) +" " + str(self.temp_list[4]) + " )"   )
    def interp(self):
        if(self.temp_list[0] == 'E'):
            self.temp_list[0] = add(1,1)
            print ( "E X " + "( if  (" + " " + str(self.temp_list[0]) + " " + str(self.temp_list[1]) + " " + str(self.temp_list[2]) + " " + " )" + " " +str(self.temp_list[3]) +" " + str(self.temp_list[4]) + " )"   )
        if(str(self.temp_list[0]) == str(add(1,1))):    
            self.temp_list[0] = add(1,1).interp()
            print ( "E X " + "( if  (" + " " + str(self.temp_list[0]) + " " + str(self.temp_list[1]) + " " + str(self.temp_list[2]) + " " + " )" + " " +str(self.temp_list[3]) +" " + str(self.temp_list[4]) + " )"   )
            if (self.temp_list[0] < self.temp_list[2] ):
                print(str(self.temp_list[3]))
            elif (self.temp_list[1] > self.temp_list[2] ):
                print(str(self.temp_list[4]))
temp =redex([add(1,1),"<",5,"TRUE","FALSE"])  
print(temp)
temp.interp()