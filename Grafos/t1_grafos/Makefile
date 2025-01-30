FLAGS = -ggdb -Werror -pg -Wextra -std=gnu11 -Wno-unused-result -mglibc -Wuninitialized -march=x86-64 -Wpedantic -Wall  

all:
	gcc -c grafos.c -o grafos.o $(FLAGS)
	gcc lucas_santana4_listaadjacencia_epidemia.c grafos.o -o lucas_santana4_listaadjacencia_epidemia $(FLAGS)

clean:
	rm -vf grafos.o lucas_santana4_listaadjacencia_epidemia lucas_santana4_t1_b1_listaadjacencia_epidemia.1por1.saida.* lucas_santana4_t1_b1_listaadjacencia_epidemia.total.saida.*

