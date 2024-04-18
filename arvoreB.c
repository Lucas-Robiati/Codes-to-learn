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
/*
struct no *Insert_recursivo(struct no *raiz, int valor)
{
	if(raiz == NULL)
		{
			struct no *new = malloc(sizeof(struct no));
			new->num = valor;
			new->dir = NULL;
			new->esq = NULL;
			new->pai = raiz;
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
*/

void Insert(struct no **raiz, int valor)
{
	if(*raiz == NULL)
	{
		*raiz = malloc(sizeof(struct no));
		(*raiz)->num = valor;
		(*raiz)->dir = NULL;
		(*raiz)->esq = NULL;
		(*raiz)->pai = *raiz;	
	}
	else
	{
		if(valor < (*raiz)->num)
		{
			Insert(&((*raiz)->esq), valor);
		}
		else
		{
			Insert(&((*raiz)->dir), valor);
		}
	}
}
//=======imprimir=======//

void Imprime1(struct no *raiz)
{
	if(raiz)
	{
		printf("%d ", raiz->num);
		Imprime1(raiz->dir);
		Imprime1(raiz->esq);
	}
}

void Imprime2(struct no *raiz)
{
	if(raiz)
	{
		Imprime2(raiz->esq);
		printf("%d ", raiz->num);
		Imprime2(raiz->dir);
	}
}

int main()
{
	struct no *raiz = NULL;
  int op, valor;

do{
	printf("\n0-Sair\n1-Inserir\n2-Imprimir\n");
	scanf("%d", &op);

	switch(op)
	{
	case 1:
		printf("\nValor a ser inserido\n");
		scanf("%d", &valor);
		Insert(&raiz, valor);
		break;
	
	case 2:
		puts("\nPrimeira impressao\n");
		Imprime1(raiz);
		printf("\n");
		puts("\nSegunda impressao\n");
		Imprime2(raiz);
		printf("\n");
		break;
	}
}while(op != 0);

return 0;
}
