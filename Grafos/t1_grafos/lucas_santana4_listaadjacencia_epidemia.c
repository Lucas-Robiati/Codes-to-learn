#include <stdio.h>
#include <stdlib.h>
#include "grafos.h"

// arquivo de saida: lucas_santana4_listaadjacencia_epidemia.1por1.saida

int main()
{
  struct Grafo *grafo = cria_grafo();
  
  ler_arquivo(grafo);

return 0;
}
