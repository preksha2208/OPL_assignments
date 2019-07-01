// Define a substitution function that plugs the value of a variable into references to that variable.(71L)
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
struct F {
   char  func[50];
};
struct D {
   char  defi[50];
};
int add(int a, int b)
{
    return('(' + '+'+ a + b + ')');
}
void main( )
{
   struct E obje;
   struct V objv;
   struct primitive objp;
   struct X objx;
   struct F objf;
   struct D objd;
   int i;
strcpy(item[0].tag, "if");
strcpy(item[0].exp, "e");
item[0].num1 = 2;
item[0].num2 = 5;
int x = 1;
int y = 1;
const char * ad = add(x,y);
if(item[0].exp == 'e')
    {
        strcpy(item[0].exp, ad);
        for(i=0;i<temp;i++)
        {
          printf("%s\t %s\t %d\t %d\t",item[i].tag,item[i].exp,item[i].num1,item[i].num2);
        }
    }
else if (item[0].exp == 'e')
    {
        for(i=0;i<temp;i++)
        {
          printf("%s\t %s\t %d\t %d\t",item[i].tag,item[i].exp,item[i].num1,item[i].num2);
        }
    }
else if (item[0].exp == 'e')
    {
        for(i=0;i<temp;i++)
        {
          printf("%s\t %s\t %d\t %d\t",item[i].tag,item[i].exp,item[i].num1,item[i].num2);
        }
    }
}