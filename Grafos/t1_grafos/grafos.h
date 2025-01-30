#ifndef _GRAFOS_H_
#define _GRAFOS_H_

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <errno.h>
#include <fcntl.h>
#include <string.h>

struct Relacao
{
  char individuo;
  int n;
  int infeccao;
  struct Relacao *proximo;
}; 

struct vertice
{
  char individuo;
  int n;
  int infeccao;
  struct vertice *vertice_proximo;
  struct Relacao *lista;                                                                                                                          
}; 

struct Grafo
{
  struct vertice **inicio;
};

struct Grafo *cria_grafo();
struct vertice *cria_vertice(int n, char novo_individuo);
struct Relacao *cria_Relacao(int n, char individuo);
struct vertice *pesquisa(struct Grafo *g, char novo_individuo);
struct vertice *insere_vertice(struct Grafo *g, int id, char novo_individuo);

void insere_lista(struct Grafo *g,int individuo1_id, char individuo1, int individuo2_id, char individuo2);
void ler_arquivo(struct Grafo *g);
void Relacao_1por1(struct Grafo *g);
void Relacao_total(struct Grafo *g);
char *tempo();

#endif
