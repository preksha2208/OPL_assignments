# REFINE YOUR DEFINITION OF CONTEXTS TO ONLY ALLOW EVALUATION CONTEXTS. (24L) 
class types :
    def __init__(self,list1):
        self.list1 = list1
    def __str__(self):
        if seld.list[0] == 'HOLE' :
            return("its a hole")
        if self.list1[1] == 'E':
            return(" the evaluation context format is type-1")
class plug :
    def __init__ (self,temp_list):
        self.temp_list = temp_list
    def __str__(self):
        if(self.temp_list[1] == 'E'):
            self.temp_list[1] = '2 < 4'
            return ("(" + str(self.temp_list[0]) + " " + "(" + " " +str(self.temp_list[1])  + " " + ")" + " " +str(self.temp_list[2]) + " " + str(self.temp_list[3]) +" " + ")")
    def interp(self):
        if(self.temp_list[1] == 'E'):
            self.temp_list[1] = '2 < 4'
            if (eval(self.temp_list[1])):
                return(str(self.temp_list[2]))
            else :
                return(str(self.temp_list[3]))
print(plug(["if","E","TRUE","FALSE"]))
print(plug(["IF","E","TRUE","FALSE"]).interp())