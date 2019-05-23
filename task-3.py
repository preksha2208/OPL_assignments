# WRITE THE TEST-SUITE OF A DOZEN J0 PRGRAMS. (69L)
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
class div:
   def __init__(self, f, g):
      self.f = f
      self.g = g
   def __str__(self):   
       return ("("+"/"+" "+str(self.f)+" "+str(self.g)+ ")")   
class sub:
   def __init__(self, h, i):
      self.h = h
      self.i = i
   def __str__(self):   
       return ("("+"-"+" "+str(self.h)+" "+str(self.i)+ ")")   
#TEST CASE 1
twelve = add(5,7)
nine = mult(1,9)
result1= mult(twelve, nine)
print(result1)
#TEST CASE 2
result2 = mult(add(1,2),mult(1,5))
print(result2)
#TEST CASE 3
result3 = mult(add(add(1, 2),mult(3,4)),10)
print(result3)
#TEST CASE 4
print(add(add(1, 1), mult(10, mult(100, 1000))))
#TEST CASE 5
print(add(10, -1))
#TEST CASE 6
print(div(sub(1, 1), mult(10, add(100, 1000))))
#TEST CASE 7
result4 = mult(7, 4)
for i in range(3):
    result4= add(result4,result4)
print(result4)
#TEST CASE 8
temp1 = sub(5,7)
temp2 = div(1,9)
result5= mult(temp1, temp2)
print(result5)
#TEST CASE 9
result6 = div(5, 7)
for i in range(5):
    result6= add(result6,result6)
print(result6)
#TEST CASE 10
result7 = div(3,9)
for i in range(2):
    result7= sub(result7,result7)
print(result7)
#TEST CASE 11
sixty_four = div(2, mult(3, add(9, sub(5, mult(7, 86)))))
print(sixty_four)
#TEST CASE 12
print(add(add(mult(97,mult(31,mult(add(28,mult(add(mult(mult(add(mult(91,mult(mult(63,40),28)),27),37),76),41),29)),33))),87),78))