// DEFINE DATA STRUCTURE TO REPRESENT J2 PROGRAMS IN LOW LEVEL. (33L) 
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
struct E {
   char  tag[50];
}; 
struct V {
   int number ;
   bool tf ; 
   char  prim[50];
};
struct primitive {
   char  sym[50];
}; 
struct X {
   char  varnam[50];
}; 
struct F {
   char  func[50];
}; 
struct D {
   char  defi[50];
}; 

 void main( ) 
{
   struct E obje;        
   struct V objv;
   struct primitive objp;
   struct X objx;        
   struct F objf;
   struct D objd;
}  