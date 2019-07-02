// DEFINE DATA STRUCTURE TO REPRESENT J3 PROGRAMS. (28L) 
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#define temp  3
struct E {
   char  tag[10];
   char  exp[10];
   int num1;
   int num2;
}item[temp];
; 
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
 void main( ) 
{        
   struct V objv;
   struct primitive objp;
   struct X objx;        
   
}  