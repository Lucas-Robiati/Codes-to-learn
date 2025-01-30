#include <stdio.h>
#include <math.h>

float anterior;
float fxanterior;
float posterior;
float fxposterior;

int 
buscainversao(float inicio, float fim, int opt)
  {
  float x = inicio;
  float fx = 0.0;

  switch(opt)
  {
    case 1:
      printf("----------------------------------\n");
      printf("|  x        | f(x) = ( (x^(3)) - (x^(2)) - 1 )     |\n");
      printf("----------------------------------\n");
      break;

    case 2:
      printf("----------------------------------\n");
      printf("|  x        | f(x) = ( e^(-x)) * ((x-1)/2) )     |\n");
      printf("----------------------------------\n");
      break;

    case 3:
      printf("----------------------------------\n");
      printf("|  x        | f(x) = ( x^(2)) - x + sen(5x))     |\n");
      printf("----------------------------------\n");
      break;

    case 4:
      printf("----------------------------------\n");
      printf("|  x        | f(x) = ( x^(2)) + 1.95x - 2.09 )     |\n");
      printf("----------------------------------\n");
      break;

    case 5:
      printf("----------------------------------\n");
      printf("|  x        | f(x) = ( x - 3 - (x^(-x)) )     |\n");
      printf("----------------------------------\n");
      break;
  }

  while(x <= fim)
  {
    switch(opt)
    {
      case 1:
        fx = (pow(x,3)) - (pow(x,2)) - 1;
        break;
      
      case 2:
        fx = (expf(x*-1.0)) * ((x-1.0)/2);
        break;
      
      case 3:
        fx = ( (pow(x,2)) - x + (sin(5*x)) );
        break;
      
      case 4:
        fx = ( (pow(x,2)) + (1.95*x) - 2.09 );
        break;
      
      case 5:
        fx = (x - 3 - (pow(x,x*-1)));
        break;
    }

    if(fx < 10.0)
    {	    
      printf("| %+f | %+f          |\n", x, fx);
    }
    if((fx >= 10.0) && (fx < 100.0))
    {
      printf("| %+f | %+f         |\n", x, fx);     
    }	    
    if(fx >= 100.0)
    {
      printf("| %+f | %+f        |\n", x, fx);     
    }	    
  
    if(x == inicio)
    {
      anterior = x;
      fxanterior = fx;
    }
    if(x != inicio) 
    {
      posterior = x;
      fxposterior = fx;
      if(((fxanterior < 0.0) && (fxposterior >= 0.0)) || ((fxanterior > 0.0) && (fxposterior <= 0.0)))
      {
        printf("----------------------------------\n"); 
        return(0);
      }
      if(fxanterior != fxposterior)
      {
        anterior = x;
        fxanterior = fx;
      }
    }

    x += 0.01;
  }
  printf("----------------------------------\n"); 
  return(0);
  }

float
dicotomia(float xa, float xb, float precisao, int opt)
  {
  float xc, anterior, f_xa, f_xb, f_xc;
  int iteracoes = 0;

  anterior = xb;
  xc = xa;

  printf("\n");  
  printf("-----------------------------------------------------------------------------\n");  
  printf("| n  | xa        | xb        | xc        | f(xa)     | f(xb)     | f(xc)     |\n");  
  printf("-----------------------------------------------------------------------------\n");  
  while(fabs(xc - anterior) > precisao)
    {
    iteracoes++;

    anterior = xc;
    xc = (xa + xb) / 2.0;

    switch(opt)
    {
      case 1:
        f_xa = (pow(xa,3)) - (pow(xa,2)) - 1;
        f_xb = (pow(xb,3)) - (pow(xb,2)) - 1;
        f_xc = (pow(xc,3)) - (pow(xc,2)) - 1;
        break;
      
      case 2:
        f_xa = (expf(xa*-1.0)) * ((xa-1)/2);
        f_xb = (expf(xb*-1.0)) * ((xb-1)/2);
        f_xc = (expf(xc*-1.0)) * ((xc-1)/2);
        break;

      case 3:
        f_xa =  ( (pow(xa,2)) - xa + (sin(5*xa)) );
        f_xb =  ( (pow(xb,2)) - xb + (sin(5*xb)) );
        f_xc =  ( (pow(xc,2)) - xc + (sin(5*xc)) );
        break;

      case 4:
        f_xa = ( (pow(xa,2)) + (1.95*xa) - 2.09 );
        f_xb = ( (pow(xb,2)) + (1.95*xb) - 2.09 );
        f_xc = ( (pow(xc,2)) + (1.95*xc) - 2.09 );
        break;

      case 5:
        f_xa = ( xa - 3 - (pow(xa,xa*-1)) );
        f_xb = ( xb - 3 - (pow(xb,xb*-1)) );
        f_xc = ( xc - 3 - (pow(xc,xc*-1)) );
        break;
    }
  
    if( iteracoes < 10)//maximo de 10 iteracoes
      {
      printf("| %d  | %+f | %+f | %+f | %+f | %+f | %+f |\n", iteracoes, xa, xb, xc, f_xa, f_xb, f_xc);
      }
    if( iteracoes >= 10)
      {
      printf("| %d | %+f | %+f | %+f | %+f | %+f | %+f |\n", iteracoes, xa, xb, xc,  f_xa, f_xb, f_xc);
      }


    if( f_xa * f_xc < 0.0)
      {
      xb = xc;
      }
    else
      {
      if( f_xb * f_xc < 0.0)
        {
        xa = xc;
        }
      }
    }
  printf("--------------------------------------------------\n");

  printf("Numero de iteracoes = %d\n", iteracoes);
  return (xc);
  }

int main()
{
  float raiz = 0.0;
  float inicio;
  float fim;
  int opt = 0;
  
  do 
  {
    printf("\nEscolha uma funcao para o metodo diclotomia\n");
    printf("0) \033[1mEncerrar\n");
    printf("1) \033[1mF: (x^(3)) - (x^(2) - 1)\n");
    printf("2) \033[1mF: (e^(-x)) * ((x-1)/2))\n");
    printf("3) \033[1mF: (x^(2)) - x + sen(5x))\n");
    printf("4) \033[1mF: (x^(2)) + 1.95x - 2.09)\n");
    printf("5) \033[1mF: (x - 3 - (x^(-x)))\n");

    printf("\n: ");
    scanf("%d", &opt);

    if(opt == 0) break;

    printf("Entre com dois pontos\n: ");
    scanf("%f", &inicio);
    printf("\n: ");
    scanf("%f", &fim);
    printf("\n");
    
    buscainversao(inicio, fim, opt);
    raiz = dicotomia(anterior, posterior, 0.0001, opt);
    printf("raiz = %.6g\n", raiz);

  }while(opt != 0);
  
  return(0);
}
