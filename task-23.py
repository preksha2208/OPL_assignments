# IMPLEMENT THE CK0 MACHINE INTERPRETER FOR J1.(25L)
class interpreter :
    def __init__ (self,temp_list):
        self.temp_list = temp_list
    def __str__(self):
        if (self.temp_list[0] == 'TRUE' ):
            return ( "[ " + str(self.temp_list[0]) + " " + "," + " " + str(self.temp_list[1])  + " " + " if [ " + str(self.temp_list[2])  + " " + str(self.temp_list[3]) + " " + str(self.temp_list[4]) + " ]" + " ]"  )
        if (self.temp_list[0] == 'FALSE'):
            return ( "[ " + str(self.temp_list[0]) + " " + "," + " " + str(self.temp_list[1])  + " " + " if [" + str(self.temp_list[2])  + " " + str(self.temp_list[3]) + " " + str(self.temp_list[4]) + " ]" + " ]"  )
        if(self.temp_list[4] == 'K0'):
            return ( "[" +str(self.temp_list[0]) + " " + str(self.temp_list[1])  + " " + str(self.temp_list[2])  + " " + str(self.temp_list[3]) + " " + str(self.temp_list[4]) + " ]"   )
        if(self.temp_list[0] == 'kif'):
            return ( "[" +str(self.temp_list[0]) + " " +str(self.temp_list[1])  + " " + str(self.temp_list[2]) + " " + str(self.temp_list[3]) + " " + str(self.temp_list[4])  + " ]"   )    
        if(self.temp_list[0] == '<' or self.temp_list[0] == '>'):
            return ( "[" +str(self.temp_list[2]) + " , " + str(self.temp_list[1])  + " (( " + str(self.temp_list[0]) + " ) , ( " + str(self.temp_list[3]) + " ) ," + str(self.temp_list[4])  + "( " + str(self.temp_list[2]) + " , "+ str(self.temp_list[3]) + " , "  + str(self.temp_list[5]) +" ) ) ]"   )    
    def interp(self):
        if(self.temp_list[0] == 'if'):
            return ( "[ " +str(self.temp_list[1]) + " " + "," + " " + "K "  + "if (" + " " + str(self.temp_list[2]) + " " + str(self.temp_list[3]) + " " + str(self.temp_list[4]) +" )" + " ]"  )    
        elif (self.temp_list[0] == 'TRUE'):
            return("[ " + str(self.temp_list[2]) + " , " + str(self.temp_list[1]) + " ]" )
        elif (self.temp_list[0] == 'FALSE'):
            return("[ " + str(self.temp_list[3]) + " , " + str(self.temp_list[1]) + " ]" )    
        elif (self.temp_list[0] == 'kif'):
            return ( "[ " +str(self.temp_list[2]) + " " + ", kapp ( () , ( " +str(self.temp_list[1])  + " " + str(self.temp_list[3]) + ") ,"  + " " + str(self.temp_list[0]) + " (" + str(self.temp_list[1]) + "," + str(self.temp_list[3]) + "," +str(self.temp_list[4]) + " ) ) ]"   )    
        elif (self.temp_list[0] == '<' and (self.temp_list[2] < self.temp_list[3]) ):
            return ( "[" +str(self.temp_list[3]) + " , " + str(self.temp_list[1])  + " (( " + str(self.temp_list[0]) + str(self.temp_list[2]) + " , ( )" + " , " + str(self.temp_list[4])  + "( " + str(self.temp_list[2]) + " , "+ str(self.temp_list[3]) + " , "  + str(self.temp_list[5]) +" ) ) ]"   )    
        elif (self.temp_list[0] == '>' and (self.temp_list[2] > self.temp_list[3]) ):
            return ( "[" +str(self.temp_list[2]) + " , " + str(self.temp_list[1])  + " (( " + str(self.temp_list[0]) + str(self.temp_list[3]) + " , ( )" + " , " + str(self.temp_list[4])  + "( " + str(self.temp_list[2]) + " , "+ str(self.temp_list[3]) + " , "  + str(self.temp_list[5]) +" ) ) ]"   )    

print(interpreter(["if","2 < 5","TRUE then 2","FALSE then 5","K0"]))
print(interpreter(["if","2 < 5","TRUE then 2","FALSE then 5","K0"]).interp())
print("\n")
print(interpreter(["TRUE","K","SATISFIED","NOT-SATISFIED","K"]))
print(interpreter(["TRUE","K","SATISFIED","NOT-SATISFIED","K"]).interp())
print("\n")
print(interpreter(["FALSE","K","SATISFIED","NOT-SATISFIED","K"]))
print(interpreter(["FALSE","K","SATISFIED","NOT-SATISFIED","K"]).interp())
print("\n")
print(interpreter(["kif","2","<","5","K0"]))
print(interpreter(["kif","2","<","5","K0"]).interp())
print("\n")
print(interpreter(["<","kapp",2,5,"Kif" , "K0"]))
print(interpreter(["<","kapp",2,5,"Kif" , "K0"]).interp())
print("\n")
print(interpreter(["if","TASK > 23","MAY CROSS F+ ","WILL GET F","K0"]))
print(interpreter(["if","TASK > 23","MAY CROSS F+","WILL GET F","K0"]).interp())
print("\n")
print(interpreter([">","kapp",5,2,"Kif" , "K0"]))
print(interpreter([">","kapp",5,2,"Kif" , "K0"]).interp())