#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define TAM 19

struct pessoa
{
	char nome[30];
	int cpf;
};

struct No
{
	struct pessoa p;
	struct No *proximo;
};

typedef struct
{
	struct No *inicio;
	int tam;
}Lista;


Lista *tabela[TAM];


//====funções hash====//

int calc_hasing(int key)
{
	return key % TAM;
}


int funcao_hash(char *str)
{
	int i, n = strlen(str);
	unsigned int hash = 0;

	for(i = 0;i < n; i++)
	{
		hash += str[i]*(i+1);
	}
	return calc_hasing(hash);
}

//=====criar tabela=====//

Lista* cria_lista()
{
	Lista *l = malloc(sizeof(Lista));
	l->inicio = NULL;
	l->tam = 0;
	return l;
}

void inicializatabela()
{
	int i;
	for(i = 0; i<TAM; i++)
	{
		tabela[i] = cria_lista();
	}
}

//======inserções====//
struct pessoa ler_pessoa()
{
	struct pessoa x;
	printf("Insira seu nome: ");
	fgets(x.nome, 30, stdin);
	printf("Insira seu CPF: ");
	scanf("%d", &x.cpf);
	return x;
}

void inserir(struct pessoa p, Lista *lista)
{
	struct No *no = malloc(sizeof(no));
	no->pessoa = p;

	no->proximo = lista->inicio;
	lista->inicio = no;
	lista->tam++;
}

void inserir_tabela()
{
	struct pessoa pes = ler_pessoa();
	int hash = funcao_hash(pes.nome);
	inserir(pes, tabela[hash]);
}

//=====funções de busca====//
struct No *buscarNo(int cpf, struct No *inicio)
{
	while(inicio != NULL)
	{
		if(inicio->pessoa.cpf == cpf)
			return inicio;

		else
			inicio = inicio->proximo;
	}
	return NULL;
}


struct pessoa *buscar_pessoa(char *busca, int CPF)
{
	int hash = funcao_hash(busca);
	struct No *no = buscarNo(CPF, tabela[hash]->inicio);
	if(no)
		return &no->pessoa;
	
	else
		return NULL;
}

//====funções de impressão===//
void imprimir_pessoa(struct pessoa p)
{
	printf("\tNome: %s\tCPF: %d\n", p.nome, p.cpf);
}


void imprimir_lista(struct No *inicio)
{
	while(inicio != NULL)
	{
		imprimir_pessoa(inicio->pessoa);
	  inicio = inicio->proximo;
	}
}

void imprimir_tabela()
{
	printf("\n-------------------------Tabela------------------\n");
	for(int i = 0; i<TAM; i++)
	{
		printf("%d Lista tamanho: %d\n", i, tabela[i]->tam);
		imprimir_lista(tabela[i]->inicio);
	}
}

//====end funções====//

int main()
{
	int registro, op;
	struct pessoa *p;

	inicializatabela();
	
	do {
		printf("\n0 - Sair / 1 - Inserir / 2 - Buscar / 3 - Imprimir tabela\n");
		scanf("%d",&op);
		switch (op)
		{
			case 0:
					printf("\nFinalizando...\n");
					break;

			case 1:
					inserir_tabela();
					break;

			case 2:
					printf("Qual pessoa deseja buscar? ");
					char temp[30];
					fgets(temp, 30, stdin);
					printf("Insira o CPF que deseja buscar: ");
					scanf("%d", &registro);
					p = buscar_pessoa(temp, registro);
					if(p)
					{
						printf("\nBusca bem sucedida\nNome:%s\n CPF: %d\n", p->nome, p->cpf);
						
					}
					else
					{
						printf("\nFalha ao encontrar a pessoa informada\n");
					}
					break;

			case 3:
					imprimir_tabela();
					break;
			default :
					printf("\nOpcao invalida!\n");
		}
	}while(op != 0);

return 0;
}
