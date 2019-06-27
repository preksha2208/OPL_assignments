# IMPLEMENT THE TEST-SUITES FOR CK0 MACHINE INTERPRETER FOR J1.(28L)
class interpreter :
    def __init__ (self,temp_list):
        self.temp_list = temp_list
    def __str__(self):
        if (self.temp_list[0] == 'TRUE' ):
            return ( "[ " + str(self.temp_list[0]) + " " + "," + " " + str(self.temp_list[1])  + " " + " if [ " + str(self.temp_list[2])  + " " + str(self.temp_list[3]) + " " + str(self.temp_list[4]) + " ]" + " ]"  )
        if (self.temp_list[0] == 'FALSE'):
            return ( "[ " + str(self.temp_list[0]) + " " + "," + " " + str(self.temp_list[1])  + " " + " if [" + str(self.temp_list[2])  + " " + str(self.temp_list[3]) + " " + str(self.temp_list[4]) + " ]" + " ]"  )
        if(self.temp_list[4] == 'K'):
            return ( "[" +str(self.temp_list[0]) + " " + str(self.temp_list[1])  + " " + str(self.temp_list[2])  + " " + str(self.temp_list[3]) + " " + str(self.temp_list[4]) + " ]"   )
    def interp(self):
        if(self.temp_list[0] == 'if'):
            return ( "[ " + "C"+str(self.temp_list[1]) + " " + "," + " " + str(self.temp_list[4])  + "if (" + " " + str(self.temp_list[2]) + " " + str(self.temp_list[3]) + " " + str(self.temp_list[4]) +" )" + " ]"  )    
        elif (self.temp_list[0] == 'TRUE'):
                return("[ " + str(self.temp_list[2]) + " , " + str(self.temp_list[1]) + " ]" )
        elif (self.temp_list[0] == 'FALSE'):
                return("[ " + str(self.temp_list[3]) + " , " + str(self.temp_list[1]) + " ]" )    
print(interpreter(["if","2 < 5","TRUE then 2","FALSE then 5","K"]))
print(interpreter(["if","2 < 5","TRUE then 2","FALSE then 5","K"]).interp())
print("\n")
print(interpreter(["if","TASK > 23","MAY CROSS F+ ","WILL GET F","K"]))
print(interpreter(["if","TASK > 23","MAY CROSS F+","WILL GET F","K"]).interp())
print("\n")
print(interpreter(["TRUE","K","SATISFIED","NOT-SATISFIED","K"]))
print(interpreter(["TRUE","K","SATISFIED","NOT-SATISFIED","K"]).interp())
print("\n")
print(interpreter(["FALSE","K","SATISFIED","NOT-SATISFIED","K"]))
print(interpreter(["FALSE","K","SATISFIED","NOT-SATISFIED","K"]).interp())