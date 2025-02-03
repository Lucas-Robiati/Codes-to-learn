CREATE EXTENSION IF NOT EXISTS pgcrypto;

DROP VIEW IF EXISTS desnormalize_v1; 
DROP TABLE IF EXISTS main_table;
DROP TABLE IF EXISTS escolaridade CASCADE;
DROP TABLE IF EXISTS sexo CASCADE;
DROP TABLE IF EXISTS co_causa_basica CASCADE;
DROP TABLE IF EXISTS desc_causa_basica CASCADE;
DROP TABLE IF EXISTS info CASCADE;
DROP TABLE IF EXISTS relacao_cidade CASCADE;

CREATE TABLE public.main_table
(
    dt_obito date NOT NULL,
    dt_nascimento date,
    nu_idade int,
    sg_sexo varchar(10),
    tp_raca_cor varchar(10),
    tp_escolaridade varchar(25),
    municipio_ibge_residencia varchar(50),
    municipio_ibge_ocorrencia varchar(50),
    co_cid_causa_basica varchar(5) NOT NULL,
    desc_cid_causa_basica varchar(50) NOT NULL,
    capitulo_cid_causa_basica varchar(60) NOT NULL,
    categoria_cid_causa_basica varchar(50) NOT NULL
);
 
\copy main_table from '/home/FatalPenguin/Codes-to-learn/psql/trabalhoBD/trabalho2/dados_cronicas_ses_2010.csv' WITH DELIMITER ';' CSV HEADER;

CREATE OR REPLACE FUNCTION Fn_Inicialize_bd()
RETURNS void
AS $$
--DECLARE  query varchar(500);
BEGIN
    RAISE INFO 'Excluindo tabelas existentes'; 


  /*CREATE TABLE public.main_table

    (
      dt_obito date NOT NULL,
      dt_nascimento date,
      nu_idade int,
      sg_sexo varchar(10),
      tp_raca_cor varchar(10),
      tp_escolaridade varchar(25),
      municipio_ibge_residencia varchar(50),
      municipio_ibge_ocorrencia varchar(50),
      co_cid_causa_basica varchar(5) NOT NULL,
      desc_cid_causa_basica varchar(50) NOT NULL,
      capitulo_cid_causa_basica varchar(60) NOT NULL,
      categoria_cid_causa_basica varchar(50) NOT NULL
    );
    
    query := '\copy main_table from ''/home/FatalPenguin/Codes-to-learn/psql/trabalhoBD/trabalho2/dados_cronicas_ses_2010.csv'' WITH DELIMITER '';'' CSV HEADER;'
    EXECUTE query;*/ 

    --COPY main_table FROM '/tmp/dados_dcronicas_ses_2010.csv' csv header delimiter ';' quote '"'; 
    RAISE INFO 'Iniciando normalizacao da main table';
    
    DELETE FROM main_table WHERE nu_idade is NULL;

    UPDATE main_table SET dt_nascimento = (dt_obito - nu_idade) WHERE dt_nascimento is NULL;
    ALTER TABLE main_table ALTER COLUMN dt_nascimento SET NOT NULL;
    ALTER TABLE main_table ALTER COLUMN nu_idade SET NOT NULL;

    UPDATE main_table SET tp_escolaridade ='Ignorado' WHERE tp_escolaridade is NULL;
    ALTER TABLE main_table ALTER COLUMN tp_escolaridade SET NOT NULL;

    UPDATE main_table SET tp_raca_cor ='Não Consta' WHERE tp_raca_cor is NULL;
    ALTER TABLE main_table ALTER COLUMN tp_raca_cor SET NOT NULL;

    UPDATE main_table SET municipio_ibge_residencia ='Não Consta' WHERE municipio_ibge_residencia is NULL;
    ALTER TABLE main_table ALTER COLUMN municipio_ibge_residencia SET NOT NULL;

    UPDATE main_table SET municipio_ibge_ocorrencia ='Não Consta' WHERE municipio_ibge_ocorrencia is NULL;
    ALTER TABLE main_table ALTER COLUMN municipio_ibge_ocorrencia SET NOT NULL;

END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION Fn_Normalize_bd() 
RETURNS void
AS $$
BEGIN
    
    CREATE TABLE escolaridade
    (
      id SERIAL PRIMARY KEY NOT NULL,
      tp_escolaridade varchar(250) NOT NULL
    );
    
    CREATE TABLE sexo
    (
      id SERIAL PRIMARY KEY NOT NULL,
      sg_sexo varchar(10)
    );
   
    CREATE TABLE co_causa_basica
    (
      id SERIAL PRIMARY KEY NOT NULL,
      co_cid_causa_basica varchar(5) NOT NULL
    ); 
    
    CREATE TABLE desc_causa_basica
    (
      id SERIAL PRIMARY KEY NOT NULL,
      desc_cid_causa_basica varchar(50) NOT NULL
    ); 
     
    CREATE TABLE info
    (
      id SERIAL PRIMARY KEY NOT NULL,
      capitulo_cid_causa_basica varchar(250) NOT NULL,
      categoria_cid_causa_basica varchar(250) NOT NULL
    );    
    
    CREATE TABLE relacao_cidade
    (
      id SERIAL PRIMARY KEY NOT NULL,
      cidade varchar(250)
    );

----tabela 1-----
    RAISE INFO 'CREATE TABLE escolaridade';
    INSERT INTO escolaridade (tp_escolaridade)
    SELECT DISTINCT tp_escolaridade FROM main_table;
    
    ALTER TABLE main_table ADD COLUMN escolaridade_id int; 
    ALTER TABLE main_table ADD CONSTRAINT fk_escolaridade_id FOREIGN KEY (escolaridade_id) 
    REFERENCES escolaridade(id);    
    
    UPDATE main_table SET escolaridade_id = escolaridade.id FROM escolaridade
    WHERE escolaridade.tp_escolaridade = main_table.tp_escolaridade; 

    RAISE INFO 'ENCRYPT COLUMN tp_escolaridade';
    UPDATE escolaridade SET tp_escolaridade = pgp_sym_encrypt(tp_escolaridade, 'senha_forte_escolaridade');

-----tabela 2------
    RAISE INFO 'CREATE TABLE sexo';
    INSERT INTO sexo (sg_sexo)
    SELECT DISTINCT sg_sexo FROM main_table;
    
    ALTER TABLE main_table ADD COLUMN sexo_id int; 
    ALTER TABLE main_table ADD CONSTRAINT fk_sexo_id FOREIGN KEY (sexo_id) 
    REFERENCES sexo(id);
    
    UPDATE main_table SET sexo_id = sexo.id FROM sexo
    WHERE sexo.sg_sexo = main_table.sg_sexo;
    
-----tabela 3------
    RAISE INFO 'CREATE TABLE co_causa_basica';
    INSERT INTO co_causa_basica (co_cid_causa_basica)
    SELECT DISTINCT co_cid_causa_basica FROM main_table;
    
    ALTER TABLE main_table ADD COLUMN co_causa_basica_id int; 
    ALTER TABLE main_table ADD CONSTRAINT fk_co_causa_id FOREIGN KEY (co_causa_basica_id) 
    REFERENCES co_causa_basica(id);
    
    UPDATE main_table SET co_causa_basica_id = co_causa_basica.id FROM co_causa_basica
    WHERE co_causa_basica.co_cid_causa_basica = main_table.co_cid_causa_basica;
    
----tabela 4-----
    RAISE INFO 'CREATE TABLE desc_causa_basica';
    INSERT INTO desc_causa_basica (desc_cid_causa_basica)
    SELECT DISTINCT desc_cid_causa_basica FROM main_table;
    
    ALTER TABLE main_table ADD COLUMN desc_causa_basica_id int; 
    ALTER TABLE main_table ADD CONSTRAINT fk_desc_causa_id FOREIGN KEY (desc_causa_basica_id) 
    REFERENCES desc_causa_basica(id);
    
    UPDATE main_table SET desc_causa_basica_id = desc_causa_basica.id FROM desc_causa_basica
    WHERE desc_causa_basica.desc_cid_causa_basica = main_table.desc_cid_causa_basica;

----tabela 5-----
    RAISE INFO 'CREATE TABLE info';
    INSERT INTO info (capitulo_cid_causa_basica, categoria_cid_causa_basica)
    SELECT DISTINCT capitulo_cid_causa_basica, categoria_cid_causa_basica FROM main_table;
 
    ALTER TABLE main_table ADD COLUMN info_id int; 
    ALTER TABLE main_table ADD CONSTRAINT fk_info_id FOREIGN KEY (info_id) 
    REFERENCES info(id);
    
    UPDATE main_table SET info_id = info.id FROM info
    WHERE info.capitulo_cid_causa_basica = main_table.capitulo_cid_causa_basica AND
    info.categoria_cid_causa_basica = main_table.categoria_cid_causa_basica;

    RAISE INFO 'ENCRYPT COLUMN capitulo_cid_causa_basica';
    UPDATE info SET capitulo_cid_causa_basica = pgp_sym_encrypt(capitulo_cid_causa_basica, 'senha_forte_capitulo'); 
    RAISE INFO 'ENCRYPT COLUMN categoria_cid_causa_basica';
    UPDATE info SET categoria_cid_causa_basica = pgp_sym_encrypt(categoria_cid_causa_basica, 'senha_forte_categoria');

----tabela 6------
    RAISE INFO 'CREATE TABLE relacao_cidade';
    INSERT INTO relacao_cidade (cidade)
    SELECT DISTINCT municipio_ibge_residencia FROM Main_table AS mt 
    UNION (SELECT DISTINCT Municipio_ibge_ocorrencia FROM Main_table);
    
    ALTER TABLE main_table ADD COLUMN residencia_id int; 
    ALTER TABLE main_table ADD CONSTRAINT fk_residencia_id FOREIGN KEY (residencia_id) 
    REFERENCES relacao_cidade(id);

    ALTER TABLE main_table ADD COLUMN ocorrencia_id int; 
    ALTER TABLE main_table ADD CONSTRAINT fk_ocorrencia_id FOREIGN KEY (ocorrencia_id) 
    REFERENCES relacao_cidade(id);

    UPDATE main_table SET residencia_id = relacao_cidade.id FROM relacao_cidade
    WHERE relacao_cidade.cidade = main_table.municipio_ibge_residencia;

    UPDATE main_table SET ocorrencia_id = relacao_cidade.id FROM relacao_cidade
    WHERE relacao_cidade.cidade = main_table.municipio_ibge_ocorrencia;
   
    RAISE INFO 'ENCRYPT COLUMN relacao_cidade';
    UPDATE relacao_cidade SET cidade = pgp_sym_encrypt(cidade, 'senha_forte_cidade');

-----DROP---
    ALTER TABLE main_table DROP COLUMN tp_escolaridade;
    ALTER TABLE main_table DROP COLUMN sg_sexo;
    ALTER TABLE main_table DROP COLUMN co_cid_causa_basica;
    ALTER TABLE main_table DROP COLUMN desc_cid_causa_basica;
    ALTER TABLE main_table DROP COLUMN categoria_cid_causa_basica;
    ALTER TABLE main_table DROP COLUMN capitulo_cid_causa_basica;
    ALTER TABLE main_table DROP COLUMN municipio_ibge_residencia;
    ALTER TABLE main_table DROP COLUMN municipio_ibge_ocorrencia;

END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION Fn_calc_idade (obt date, nasc date) 
RETURNS int
AS $$
BEGIN
    RETURN EXTRACT (YEAR FROM AGE(obt, nasc));
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION Fn_created_view_bd() 
RETURNS TABLE
   (
    dt_obito date,
    dt_nascimento date,
    nu_idade int,
    sg_sexo varchar(10),
    tp_raca_cor varchar(10),
    tp_escolaridade varchar(25),
    municipio_ibge_residencia varchar(50),
    municipio_ibge_ocorrencia varchar(50),
    co_cid_causa_basica varchar(5),
    desc_cid_causa_basica varchar(50),
    capitulo_cid_causa_basica varchar(60),
    categoria_cid_causa_basica varchar(50)
   )
AS $$
BEGIN
    CREATE VIEW desnormalize_v1 AS
    SELECT main.dt_obito, main.dt_nascimento, main.nu_idade, sexo.sg_sexo, main.tp_raca_cor,
    pgp_sym_decrypt(escolaridade.tp_escolaridade::bytea, 'senha_forte_escolaridade')::varchar AS tp_escolaridade, 
    pgp_sym_decrypt(residencia.cidade::bytea, 'senha_forte_cidade')::varchar AS municipio_ibge_residencia,
    pgp_sym_decrypt(ocorrencia.cidade::bytea, 'senha_forte_cidade')::varchar AS municipio_ibge_ocorrencia,
    co_causa_basica.co_cid_causa_basica, desc_causa_basica.desc_cid_causa_basica,  
    pgp_sym_decrypt(info.capitulo_cid_causa_basica::bytea, 'senha_forte_capitulo')::varchar AS capitulo_cid_causa_basica, 
    pgp_sym_decrypt(info.categoria_cid_causa_basica::bytea, 'senha_forte_categoria')::varchar AS categoria_cid_causa_basica
    FROM main_table AS main 
    JOIN escolaridade ON main.escolaridade_id = escolaridade.id
    JOIN sexo ON main.sexo_id = sexo.id
    JOIN co_causa_basica ON main.co_causa_basica_id = co_causa_basica.id
    JOIN desc_causa_basica ON main.desc_causa_basica_id = desc_causa_basica.id
    JOIN info ON main.info_id = info.id
    JOIN relacao_cidade AS residencia ON main.residencia_id = residencia.id
    JOIN relacao_cidade AS ocorrencia ON main.ocorrencia_id = ocorrencia.id;
    
    RETURN QUERY SELECT * FROM desnormalize_v1 limit 50; 
END;
$$ LANGUAGE plpgsql;



---Chamada de funcoes-----
SELECT Fn_Inicialize_bd();
SELECT Fn_Normalize_bd();
SELECT * FROM Fn_created_view_bd();


