# WRITE A PRETTY-PRINTER FOR J0 PROGRAM. (17L)
class number:
   def __init__(self,a):
      self.a = a
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
fifteen = mult(add(1,2),mult(1,5))
print(fifteen)