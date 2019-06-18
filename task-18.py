#  IMPLEMENT THE CC0 MACHINE INTERPRETER FOR J1. (35L)
class interpreter :
    def __init__ (self,temp_list):
        self.temp_list = temp_list
    def __str__(self):
        if(self.temp_list[4] == 'E'):
            return ( "[" +str(self.temp_list[0]) + " " + str(self.temp_list[1])  + " " + str(self.temp_list[2])  + " " + str(self.temp_list[3]) + " " + str(self.temp_list[4]) + " ]"   )
        elif (self.temp_list[1] == 'E' and self.temp_list[2] == 'HOLE'):
            self.temp_list[2] = "2 < 5"
            return ( "[ " + str(self.temp_list[0]) + " " + "," + " " + str(self.temp_list[1])  + " " + " [ if " + str(self.temp_list[2])  + " " + str(self.temp_list[3]) + " " + str(self.temp_list[4]) + " ]" + " ]"  )
        elif (self.temp_list[1] == 'E' and self.temp_list[2] == 'HOLE'):
            self.temp_list[2] = "2 < 5"
            return ( "[ " + str(self.temp_list[0]) + " " + "," + " " + str(self.temp_list[1])  + " " + " [ if " + str(self.temp_list[2])  + " " + str(self.temp_list[3]) + " " + str(self.temp_list[4]) + " ]" + " ]"  )
    def interp(self):
        if(self.temp_list[0] == 'if'):
            return ( "[ " + str(self.temp_list[1]) + " " + "," + " " + str(self.temp_list[4])  + " " + " [ if " + " HOLE "  + " " + str(self.temp_list[2]) + " " + str(self.temp_list[3]) + " ]" + " ]"  )    
        elif (self.temp_list[0] == 'TRUE'  and self.temp_list[2] == 'HOLE'):
            self.temp_list[2] = " 2 < 5 "
            if (eval(self.temp_list[2])):
                return("[ " + str(self.temp_list[3]) + " , " + str(self.temp_list[1]) + " ]" )
            else:
                return("[ " + str(self.temp_list[4]) + " , " + str(self.temp_list[1]) + " ]" )
        elif (self.temp_list[0] == 'FALSE'  and self.temp_list[2] == 'HOLE'):
            self.temp_list[2] = " 5 < 2 "
            if (eval(self.temp_list[2])):
                return("[ " + str(self.temp_list[3]) + " , " + str(self.temp_list[1]) + " ]" )
            else:
                return("[ " + str(self.temp_list[4]) + " , " + str(self.temp_list[1]) + " ]" )

print(interpreter(["if","2 < 5","TRUE","FALSE","E"]))
print(interpreter(["if","2 < 5","TRUE","FALSE","E"]).interp())
print("\n")
print(interpreter(["TRUE","E","HOLE","TRUE","FALSE"]))
print(interpreter(["TRUE","E","HOLE","TRUE","FALSE"]).interp())
print("\n")
print(interpreter(["FALSE","E","HOLE","TRUE","FALSE"]))
print(interpreter(["FALSE","E","HOLE","TRUE","FALSE"]).interp())