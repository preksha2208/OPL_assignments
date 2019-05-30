#  DEFINE DATA STRUCTURES TO REPRESENT SEXPRS. (10L) 
class sexpr: pass
class emptystring(sexpr):
      empty_tuple = () 
      print (empty_tuple)
class strings(sexpr):
      strng = "sexpr"
      print(strng)
class pair(sexpr):
      tup1 = ('string1', 'string2')
      print(tup1)