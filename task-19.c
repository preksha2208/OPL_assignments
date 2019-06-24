// DEFINE DATA STRUCTURE TO REPRESENT J1 PROGRAMS. (20L) 
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
 void main( ) 
{
   struct E obje;        
   struct V objv;
   struct primitive objp;
}  