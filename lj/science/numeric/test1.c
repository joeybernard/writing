#include <stdio.h>
#include <stdlib.h>

int main (int argc, char **argv) {
   int count = atoi(argv[1]);
   int count2 = 100000000;
   int ans = 0;
   for (int i=0; i < count2; i++) {
      ans =+ (i-1)^(i-1);
   }
}

