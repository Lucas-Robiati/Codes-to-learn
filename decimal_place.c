/*
	Name: Lucas Robiati Sant' Ana
	
		O código em questão manipula strings com o intuito de possibilitar
	a escolha de quantas casas decimais serão impressas por um determinado programa.
*/

#include<stdio.h>
#include<string.h>


int main()
{
long double n = 2.123456789; 
char t[] = {"a saida e %."};
char numero;
char f[] = {"llf\n"};
scanf("%hhd", &numero);
char cont[18];
numero += '0';

strcpy(cont, t);
cont[12]=numero;
strcat(cont, f);

printf(cont, n);



return 0;
}

 
 
