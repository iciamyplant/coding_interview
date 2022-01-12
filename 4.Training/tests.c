#include <stdio.h>

int main()
{
    char str[4];
    str[0]='a';
    str[1]='a';
    str[2]='a';
    str[3] =-'+';
    int i =0;
    char c ='+'; //43 dans le man ascii
    char d =-'+'; //
    printf("unsigned char c : %d\n", (unsigned char)c);
    printf("signed char c: %d\n", (signed char)c);
    printf("char d: %d\n", d);
    printf("unsigned char d: %d\n", (unsigned char)d);
    printf("signed char d: %d\n", (signed char)d);
    printf("(unsigned char)-1%d\n", (unsigned char)-1);
    int test=d;
    printf("%d\n", test);
    test=(unsigned int)test;
    printf("%d\n", test);
    printf("%u\n", test);
    while (str[i])
    {
        printf("str[%d]: %d\n",i, str[i]);
        i++;
    }
}

//128 caracteres dans le man ascii
//0 à 255 pour les unsigned char
//-127 à 127 pour les signed char
//Là où, sur toutes les plateformes, int équivaut à signed int, short équivaut à signed short et long équivaut à signed long
//le type char n'équivaut pas nécessairement au type signed char
// selon les plateformes, le type char sera soit signé, soit non signé