# REFINE FIND-REDEX SO THAT IT LOOKS FOR EVALUATION CONTEXTS. (13L) 
def redex(temp_list):
    if(str(temp_list[1]) == '2 < 4'):
        temp_list[1] = "E"
         return ("(" + str(self.temp_list[0]) + " " + "(" + " " +str(self.temp_list[1])  + " " + ")" + " " +str(self.temp_list[2]) + " " + str(self.temp_list[3]) +" " + ")")
    def interp(self):
        if(self.temp_list[1] == 'E'):
            self.temp_list[1] = '2 < 4'
            if (eval(self.temp_list[1])):
                return(str(self.temp_list[2]))
            else :
                return(str(self.temp_list[3]))
print(redex(["if ","2 < 4","TRUE","FALSE"]))
print(redex(["IF","2 < 4","TRUE","FALSE"]).interp())