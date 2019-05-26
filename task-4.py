# WRITE A BIG-SEP INTERPRETER FOR J0 PROGRAM. (23L)
class number:
   def __init__(self,a):
      self.a = a
   def interp(self):
       return self.a
class mult:
   def __init__(self, b, c):
      self.b = b
      self.c = c
   def interp(self):
      return self.b.interp() * self.c.interp()
   def __str__(self):   
       return ("("+"*"+" "+str(self.b)+" "+str(self.c)+ ")")  
class add:
   def __init__(self, d, e):
        self.d = d
        self.e = e 
   def interp(self):
      return self.d.interp() + self.e.interp()
   def __str__(self):
       return ("("+"+"+" "+str(self.d)+" "+str(self.e)+ ")")  
print(mult(add(1,2),mult(1,5)))
print(mult(add(number(1),number(2)),mult(number(1),number(5))).interp())