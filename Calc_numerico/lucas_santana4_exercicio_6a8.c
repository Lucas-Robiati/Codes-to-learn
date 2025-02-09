#include <stdio.h> 
#include <stdlib.h>
#include <math.h> 

float f_x(float x, int opt)
{
  float y;
  
  switch(opt)
  {
    case 1:
      y = ( (2 * x) - (cos(x)) );
      break;
    
    case 2:
      y = expf(x) + (0.5 * x);
      break;

    case 3:
      y = ( (5*(pow(x,4))) - (sin(x)) );
      break;
  }
  
  return(y);
} 

float derivada_f_x(float x, int opt)
{
  float y;
  
  switch(opt)
  {
    case 1:
      y = ( 2 - (sin(x) * -1.0) );
      break;
    
    case 2:
      y = expf(x) + 0.5;
      break;

    case 3:
      y = ( (20*(pow(x,3))) - (cos(x)) );
      break;
  }
  
  return(y);
}

float newtonraphson(float x0, float precisao, int opt)
  {

  float x1, x1_anterior;
  int iteracoes = 0;

  x1_anterior = 2 * precisao;
  printf("i, xi, xi+1, precisao\n");
  
  while( fabs(x0 - x1_anterior) > precisao )
    {
      x1_anterior = x0;
      x1 = x0 - ( f_x(x0, opt)/derivada_f_x(x0, opt) );
      x0 = x1;

      iteracoes++;
      printf("%d, %f, %f, %f\n", iteracoes, x1_anterior, x1, precisao);
    }

  return(x1);
  }

int main()
  {
  float raiz;
  float x;
  float precisao = 0.0001; // Precisao de 4 casas decimais

  int opt = 0;

  do
  {
    printf("\nEscolha uma funcao para o metodo Newton-Raphson\n");
    printf("0) \033[1mEncerrar\n");
    printf("1) \033[1mF: (2 * x) - (cos(x))\n");
    printf("2) \033[1mF: (expf(x) + (0.5 * x))\n");
    printf("3) \033[1mF: ((5*(pow(x,4))) - (sin(x)))\n");

    printf("\n: ");
    scanf("%d", &opt);
    //1-x = 0.3927; 2-x = -0.85; 3-x = 0.5;
    if(opt == 0) break;
    printf("Entre com um valor para x: ");
    scanf("%f", &x);

    printf("\nValor para x: %.4f", x);
    raiz = newtonraphson(x, precisao, opt);
    printf("raiz = %g\n", raiz);
 

  }while(opt != 0);
  
  return 0;
  }
