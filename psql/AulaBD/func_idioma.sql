
/*
  AS linhas comentadas fazem a insercao sem repeticao de idioma
porem limita a entrada de pessoas a fim de evitar um loop infinito.
  Caso queira dar uma olhada decomente da linha 20 a 30, da mesma forma 
comentando as linhas 31 e 32
 */

DELETE FROM idioma_funcionario;

CREATE OR REPLACE FUNCTION Fn_Insere_Idioma_Funcionarios (p_idioma varchar(5), p_percentual numeric(6,3))
RETURNS integer
AS $$

DECLARE
  quant_funcionarios integer;
  return_idioma integer;
  id_func integer;
BEGIN
    quant_funcionarios := (SELECT COUNT(pessoa_id) FROM funcionario);    
    quant_funcionarios := quant_funcionarios*(p_percentual/100);   

    IF ((SELECT COUNT(sigla) FROM idioma WHERE idioma.sigla=p_idioma) = 0 ) THEN
        return 0;
    END IF;

   /* FOR i IN 1..quant_funcionarios LOOP
      id_func := (SELECT pessoa_id FROM funcionario ORDER BY RANDOM() limit 1);
        
      IF ((SELECT id FROM idioma_funcionario AS t WHERE t.pessoa_id = id_func AND p_idioma=t.idioma) IS NOT NULL) THEN
          i := i - 1;
          continue;
        END IF;
      
      INSERT INTO idioma_funcionario (pessoa_id, idioma) VALUES (id_func, p_idioma);
        
    END LOOP;*/
    INSERT INTO idioma_funcionario (pessoa_id, idioma) 
    SELECT pessoa_id, p_idioma FROM funcionario ORDER BY RANDOM() limit quant_funcionarios;
    
    RETURN quant_funcionarios;
END;
$$ LANGUAGE plpgsql;

ALTER TABLE idioma_funcionario ALTER COLUMN idioma TYPE varchar(5);
ALTER TABLE idioma_funcionario DROP COLUMN  id;
ALTER TABLE idioma_funcionario ADD COLUMN id serial PRIMARY KEY;

SELECT Fn_Insere_Idioma_Funcionarios('pt-BR',90); 
SELECT Fn_Insere_Idioma_Funcionarios('pt-PT',77.5); 
SELECT Fn_Insere_Idioma_Funcionarios('en-US',60); 
SELECT Fn_Insere_Idioma_Funcionarios('es',70); 
SELECT Fn_Insere_Idioma_Funcionarios('fr',30);
SELECT Fn_Insere_Idioma_Funcionarios('ru',0); 
SELECT Fn_Insere_Idioma_Funcionarios('it',40); 
SELECT Fn_Insere_Idioma_Funcionarios('de',30);
SELECT Fn_Insere_Idioma_Funcionarios('ja',10); 
SELECT Fn_Insere_Idioma_Funcionarios('zh-CN',1);

SELECT idioma.sigla, idioma.nome, COUNT(idioma_funcionario.idioma) AS quantidade 
FROM idioma_funcionario JOIN idioma ON idioma_funcionario.idioma=idioma.sigla GROUP BY 1,2 ORDER BY 3 DESC;


