#include "grafos.h"

struct Grafo *cria_grafo()
{
  struct Grafo *novo = (struct Grafo *) calloc(1,sizeof(struct Grafo));
  novo->inicio = (struct vertice **) calloc(1, sizeof(struct vertice *));
  *novo->inicio = NULL;
  return novo;
}

struct vertice *cria_vertice(int n, char novo_individuo)
{
  struct vertice *novo = (struct vertice*) malloc(sizeof(struct vertice));
  novo->individuo = novo_individuo;
  novo->n = n;
  novo->vertice_proximo = NULL;
  novo->lista = NULL;
  
  if(n == 0 || n == 1)
  {
    novo->infeccao = 0;
  }
  if(n == 2 || n == 3)
  {
    novo->infeccao = 100;
  }

  return novo;
}

struct Relacao *cria_Relacao(int n, char individuo)
{
  struct Relacao *novo = (struct Relacao*) malloc(sizeof(struct Relacao));
  novo->individuo = individuo;
  novo->n = n;
  novo->proximo = NULL;
  
  if(n == 0 || n == 1)
  {
    novo->infeccao = 0;
  }
  if(n == 2 || n == 3)
  {
    novo->infeccao = 100;
  }

  return novo;
}

char *tempo(char *buffer)
{
  time_t rawtime;
  struct tm *info;

  time(&rawtime);
  info = localtime(&rawtime);
  strftime(buffer,20,"%Y%m%d%H%M%S%z", info);
  return buffer;
}

void Relacao_1por1(struct Grafo *g)
{
  char buffer[20];
  tempo(buffer);
  char arquivo[100] = {"lucas_santana4_t1_b1_listaadjacencia_epidemia.1por1.saida."};
  char *ptr = strcat(arquivo,buffer);
  FILE *saida = fopen(ptr,"w");

  struct vertice *aux = *g->inicio;
  char p = '%';

  while(aux != NULL)
  {
    struct Relacao *temp = aux->lista;
    int mascaras = 0;
    
    while(temp != NULL)
    {
      int soma;
      if(aux->infeccao == 100)
      {
        soma = 100;
      }
      
      else
      {
        if(aux->n == 1)
        {
          mascaras = 2;
        }

        if((temp->n == 1) || (temp->n == 2))
        {
          mascaras += 2;
        }
        
        if(mascaras != 0)
        {
          soma = ((aux->infeccao + temp->infeccao)/mascaras);
        }
      
        if(mascaras == 0)
        {
          soma = (aux->infeccao + temp->infeccao);
        }
      }

      fprintf(saida,"%c -> %c: %d%c\n", aux->individuo, temp->individuo, soma, p);
      mascaras = 0;
      temp = temp->proximo;
    }

    aux = aux->vertice_proximo;
  }

  fclose(saida);
}

//=======relacao_total===========//

void Relacao_total(struct Grafo *g)
{
  char buffer[20];
  tempo(buffer);
  char arquivo[100] = {"lucas_santana4_t1_b1_listaadjacencia_epidemia.total.saida."};
  char *ptr = strcat(arquivo,buffer);
  FILE *saida = fopen(ptr,"w");

  struct vertice *aux = *g->inicio;
  char p = '%';

  while(aux != NULL)
  {
    struct Relacao *temp = aux->lista;
    int mascaras = 0;
    int somaf = 0;
    
    while(temp != NULL)
    {
      int soma;
      if(aux->infeccao == 100)
      {
        somaf = 100;
        break;
      }

      if(aux->n == 1)
      {
        mascaras = 2;
      }

      if(temp->n == 1)
      {
        mascaras += 2;
      }
      
      if(mascaras != 0)
      {
        soma = ((aux->infeccao + temp->infeccao)/mascaras);
      }
      
      if(mascaras == 0)
      {
        soma = (aux->infeccao + temp->infeccao);
      }
      
      if(soma > somaf) somaf = soma;
      temp = temp->proximo;
    }

    aux->infeccao = somaf;
    fprintf(saida,"%c: %d%c\n", aux->individuo, aux->infeccao, p);
    aux = aux->vertice_proximo;
  }
  fclose(saida);
}

struct vertice *pesquisa(struct Grafo *g, char novo_individuo)
{

  if((g == NULL) || (*g->inicio == NULL))
  {
    return NULL;
  }
    
  struct vertice *aux = *g->inicio;
  while(aux->vertice_proximo != NULL)
  {
    if(aux->individuo == novo_individuo)
    {
      return aux; 
    }
    else
    {
      aux = aux->vertice_proximo;
    }
  }
  return ((aux->individuo == novo_individuo) ? aux : NULL);
}

//=====================================================================

struct vertice *insere_vertice(struct Grafo *g,int id, char novo_individuo)
{
  if(g == NULL)
  {
    return NULL;
  }
  
  if(*g->inicio == NULL)
  { 
    struct vertice *aux = cria_vertice(id, novo_individuo);  
    *g->inicio = aux;
    return (*g->inicio);
  }
  
  struct vertice *consulta = pesquisa(g, novo_individuo);
  if(consulta == NULL)
  { 
    struct vertice *aux = *g->inicio;
    while(aux->vertice_proximo != NULL)
    {
      if(aux->vertice_proximo->individuo > novo_individuo)
      {
        struct vertice *aux2 = aux->vertice_proximo;
        aux = cria_vertice(id, novo_individuo);
        aux->vertice_proximo = aux2;
        return aux;
      }
      else
      {
        aux = aux->vertice_proximo;
      }
    }
    aux->vertice_proximo = cria_vertice(id, novo_individuo);  
    return aux->vertice_proximo;
  }
  return consulta;
}


void insere_lista(struct Grafo *g,int individuo1_id, char individuo1, int individuo2_id, char individuo2)
{
  struct vertice *v1 = insere_vertice(g, individuo1_id, individuo1);
  struct vertice *v2 = insere_vertice(g, individuo2_id, individuo2);

  if(v1 == NULL)
  {
    printf("Grafo nao foi criado...");
  }

  if(v1->lista == NULL)
  {
    v1->lista = cria_Relacao(individuo2_id, individuo2);
  }
  else
  {
    int existe = 0;
    struct Relacao *aux = v1->lista;
    while(aux->proximo != NULL)
    {
      if(aux->individuo == individuo2)
      {
        existe = 1;
      }
      aux = aux->proximo;
    }
    if(existe != 1)
    {
      aux->proximo = cria_Relacao(individuo2_id, individuo2);
    }
  }

//relacao individuo 2

  if(v2->lista == NULL)
  {
    v2->lista = cria_Relacao(individuo1_id, individuo1);
  }
  else
  {
    int existe = 0;
    struct Relacao *aux = v2->lista;
    while(aux->proximo != NULL)
    {
      if(aux->individuo == individuo1)
      {
        existe = 1;
      }
      aux = aux->proximo;
    }
    if(existe != 1)
    {
      aux->proximo = cria_Relacao(individuo1_id, individuo1);
    }
  }

}

void ler_arquivo(struct Grafo *g)
{
  FILE *arquivo = fopen("t1_b1_listaadjacencia_epidemia.csv","r");

  int R1, R2;
  char Ind1, Ind2;
  while( (fscanf(arquivo, "%c,%d,%c,%d\n", &Ind1, &R1, &Ind2, &R2)) != -1)
  {
    insere_lista (g,R1,Ind1,R2,Ind2);
  } 

  fclose(arquivo);
  Relacao_1por1(g);
  Relacao_total(g); 
}
