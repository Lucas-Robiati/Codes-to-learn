#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

#define n 12
#define max n/2

int tmp;
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

void compara(int *v)
{
  pthread_mutex_lock(&mutex);

  int index = tmp;
  tmp = tmp + 2;

  if ((index + 1 < n) && (v[index] > v[index+1]))
  {
    int aux;
    aux = v[index];
    v[index] = v[index + 1];
    v[index + 1] = aux;
  }
  pthread_mutex_unlock(&mutex);
}

void brick_sort(pthread_t *threads, int *v)
{
 
  for(int i = 1; i <= n; i++)
  {
    
    if(i % 2 != 0)
      {
        tmp = 0;
        
        for (int j = 0; j < max; j++)
            {
              pthread_create(&threads[j], NULL, (void *)&compara, (void *)v);
            }
        
        for (int j = 0; j < max; j++)
            {
              pthread_join(threads[j], NULL);
            }
      }

      else
        {
         tmp = 1;
        
        for (int j = 0; j < max; j++)
            {
              pthread_create(&threads[j], NULL, (void *)&compara, (void *)v);
            }
        
        for (int j = 0; j < max; j++)
            {
              pthread_join(threads[j], NULL);
            }
        }
  }
}

void printV(int *v)
{
  for (int i=0; i < n; i++)
    {
      printf("%d ", v[i]);
    }
  printf("\n");
}


int main()
{
  int v[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1};

  printf("vetor desordenado: ");
  printV(v);

  pthread_t threads[max];
  brick_sort(threads, v);
  
  printf("vetor ordenado: ");
  printV(v);

return 0;
}
