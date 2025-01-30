
DROP TABLE IF EXISTS main_table;

CREATE TABLE public.main_table
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
);

set client_encoding to 'latin1';
\copy main_table from '/home/FatalPenguin/codigos/psql/trabalhoBD/trabalho2/dados_cronicas_ses_2010.csv' WITH DELIMITER ';' CSV HEADER;

--select distinct * from main_table where nu_idade is NULL order by 1;
