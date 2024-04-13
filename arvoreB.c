#include<stdio.h>
#include<stdlib.h>

struct no
{
	int num;
	struct no *dir;
	struct no *esq;
	struct no *pai;
};

//======Funções========//

struct no *Insert_recursivo(struct no *raiz, int valor)
{
	if(raiz == NULL)
		{
			struct no *new = malloc(sizeof(struct no));
			new->num = valor;
			new->dir = NULL;
			new->esq = NULL;
			new->pai = NULL;
			return new;
		}
	
	else
		{
			if(valor > raiz->num)
				{
					raiz->esq = Insert_recursivo(raiz->esq, valor);
				}
		
			if(valor < raiz->num)
				{
					raiz->dir = Insert_recursivo(raiz->dir, valor);
				}
			return raiz;
		}
}


int main()
{
	struct no *raiz = NULL;


return 0;
}
