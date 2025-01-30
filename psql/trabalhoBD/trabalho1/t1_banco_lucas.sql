CREATE DATABASE transporte_hora;
\c transporte_hora;

DROP TABLE IF EXISTS main_table;
DROP TABLE IF EXISTS dados CASCADE;
DROP TABLE IF EXISTS hora CASCADE;
DROP TABLE IF EXISTS sent CASCADE;
DROP TABLE IF EXISTS date_table CASCADE;
DROP TABLE IF EXISTS meses CASCADE;
DROP TABLE IF EXISTS veiculo CASCADE;
DROP TABLE IF EXISTS semanas CASCADE;

CREATE TABLE public.main_table (
    cnpj varchar(20) NULL,
    razao_social varchar(250) NULL,
    data_autorizacao date NULL,
    prefixo varchar(10) NULL,
    descricao varchar(250) NULL,
    tipo_veiculo varchar(250) NULL,
    sentido varchar(10) NULL,
    horario varchar(6) NULL,
    segunda_feira char NULL,
    terca_feira char NULL,
    quarta_feira char NULL,
    quinta_feira char NULL,
    sexta_feira char NULL,
    sabado char NULL,
    domingo char NULL,
    janeiro char NULL,
    fevereiro char NULL,
    marco char NULL,
    abril char NULL,
    maio char NULL,
    junho char NULL,
    julho char NULL,
    agosto char NULL,
    setembro char NULL,
    outubro char NULL,
    novembro char NULL,
    dezembro char NULL 
);

set client_encoding to 'latin1';
\copy main_table from '/home/FatalPenguin/codigos/psql/trabalhoBD/encoded-dados.csv' WITH DELIMITER ';' CSV HEADER;

SELECT * INTO dados FROM main_table;
ALTER TABLE dados ADD COLUMN id serial;

UPDATE dados SET
janeiro = COALESCE(janeiro,'-'),
fevereiro = COALESCE(fevereiro,'-'),
marco = COALESCE(marco,'-'),
abril = COALESCE(abril,'-'),
maio = COALESCE(maio,'-'),
junho = COALESCE(junho,'-'),
julho = COALESCE(julho,'-'),
agosto = COALESCE(agosto,'-'),
setembro = COALESCE(setembro,'-'),
outubro = COALESCE(outubro,'-'),
novembro = COALESCE(novembro,'-'),
dezembro = COALESCE(dezembro,'-')
WHERE
janeiro IS NULL OR
fevereiro IS NULL OR
marco  IS NULL OR
abril  IS NULL OR
maio  IS NULL OR
junho  IS NULL OR
julho  IS NULL OR
agosto  IS NULL OR
setembro IS NULL OR
outubro  IS NULL OR
novembro IS NULL OR
dezembro IS NULL;

UPDATE dados SET
segunda_feira = COALESCE(segunda_feira,'-'),
terca_feira = COALESCE(terca_feira,'-'),
quarta_feira = COALESCE(quarta_feira,'-'),
quinta_feira = COALESCE(quinta_feira,'-'),
sexta_feira = COALESCE(sexta_feira,'-'),
sabado = COALESCE(sabado,'-'),
domingo = COALESCE(domingo,'-')
WHERE
segunda_feira IS NULL OR
terca_feira IS NULL OR
quarta_feira IS NULL OR
quinta_feira IS NULL OR
sexta_feira IS NULL OR
sabado IS NULL OR
domingo IS NULL;

CREATE TABLE sent
(
    id SERIAL PRIMARY KEY,
    sentido varchar(10) NULL
);

CREATE TABLE hora
(
  id SERIAL PRIMARY KEY,
  sentido varchar(10) NULL,
  horario varchar(6) NULL
);

INSERT INTO sent (sentido) 
SELECT DISTINCT sentido FROM dados;

INSERT INTO hora (horario, sentido)
SELECT DISTINCT horario, sentido FROM dados;

ALTER TABLE dados ADD COLUMN hr_id int; 
ALTER TABLE dados ADD CONSTRAINT fk_hr_id FOREIGN KEY (hr_id) 
REFERENCES hora(id); 

UPDATE dados SET hr_id = hora.id FROM hora
WHERE hora.horario = dados.horario;

ALTER TABLE hora ADD COLUMN hs_id int;
ALTER TABLE hora ADD CONSTRAINT fk_hs_id FOREIGN KEY (hs_id) 
REFERENCES sent(id);

UPDATE hora SET hs_id = sent.id FROM sent 
WHERE sent.sentido = hora.sentido;

CREATE TABLE date_table
(
    id SERIAL PRIMARY KEY,
    data_autorizacao date NULL
);

INSERT INTO date_table (data_autorizacao) 
SELECT DISTINCT data_autorizacao From dados;

ALTER TABLE dados ADD COLUMN data_id int; 
ALTER TABLE dados ADD CONSTRAINT fk_data_id FOREIGN KEY (data_id) 
REFERENCES date_table(id); 

UPDATE dados SET data_id = date_table.id FROM date_table
WHERE date_table.data_autorizacao = dados.data_autorizacao;

CREATE TABLE veiculo
(
    id SERIAL PRIMARY KEY,
    tipo_veiculo varchar(250) NULL
);

INSERT INTO veiculo (tipo_veiculo) 
SELECT DISTINCT tipo_veiculo From dados;

ALTER TABLE dados ADD COLUMN veiculo_id int; 
ALTER TABLE dados ADD CONSTRAINT fk_veiculo_id FOREIGN KEY (veiculo_id) 
REFERENCES veiculo(id);

UPDATE dados SET veiculo_id = veiculo.id FROM veiculo
WHERE veiculo.tipo_veiculo = dados.tipo_veiculo;

CREATE TABLE meses 
(
    id SERIAL PRIMARY KEY,
    janeiro char NULL,
    fevereiro char NULL,
    marco char NULL,
    abril char NULL,
    maio char NULL,
    junho char NULL,
    julho char NULL,
    agosto char NULL,
    setembro char NULL,
    outubro char NULL,
    novembro char NULL,
    dezembro char NULL
);

INSERT INTO meses 
(
    janeiro, fevereiro, marco, abril, maio, junho, julho,
    agosto, setembro, outubro, novembro, dezembro
)
SELECT DISTINCT janeiro, fevereiro, marco, abril, maio, junho, julho,
    agosto, setembro, outubro, novembro, dezembro FROM dados;

ALTER TABLE dados ADD COLUMN meses_id int; 
ALTER TABLE dados ADD CONSTRAINT fk_meses_id FOREIGN KEY (meses_id) REFERENCES meses(id); 

UPDATE dados SET meses_id = meses.id FROM meses 
WHERE  meses.janeiro = dados.janeiro AND
meses.fevereiro = dados.fevereiro AND
meses.marco = dados.marco AND
meses.abril = dados.abril AND
meses.maio = dados.maio AND
meses.junho = dados.junho AND
meses.julho = dados.julho AND 
meses.agosto = dados.agosto AND
meses.setembro = dados.setembro AND
meses.outubro = dados.outubro AND
meses.novembro = dados.novembro AND
meses.dezembro = dados.dezembro;

CREATE TABLE semanas
(
    id SERIAL PRIMARY KEY,
    segunda_feira char NULL,
    terca_feira char NULL,
    quarta_feira char NULL,
    quinta_feira char NULL,
    sexta_feira char NULL,
    sabado char NULL,
    domingo char NULL
);

INSERT INTO semanas
(
    segunda_feira,
    terca_feira,
    quarta_feira,
    quinta_feira,
    sexta_feira,
    sabado,
    domingo
)
SELECT DISTINCT segunda_feira, terca_feira, quarta_feira,
quinta_feira, sexta_feira, sabado, domingo FROM dados;

ALTER TABLE dados ADD COLUMN semanas_id int;
ALTER TABLE dados ADD CONSTRAINT fk_semanas_id FOREIGN KEY (semanas_id) 
REFERENCES semanas(id);

UPDATE dados SET semanas_id = semanas.id FROM semanas
WHERE semanas.segunda_feira = dados.segunda_feira AND
semanas.terca_feira = dados.terca_feira AND
semanas.quarta_feira = dados.quarta_feira AND
semanas.quinta_feira = dados.quinta_feira AND
semanas.sexta_feira = dados.sexta_feira AND
semanas.sabado = dados.sabado AND
semanas.domingo = dados.domingo;

---------DROPS-----------
ALTER TABLE hora DROP COLUMN sentido;
ALTER TABLE dados DROP COLUMN sentido;
ALTER TABLE dados DROP COLUMN horario;
ALTER TABLE dados DROP COLUMN data_autorizacao;
ALTER TABLE dados DROP COLUMN tipo_veiculo;

ALTER TABLE dados DROP COLUMN janeiro;
ALTER TABLE dados DROP COLUMN fevereiro;
ALTER TABLE dados DROP COLUMN marco;
ALTER TABLE dados DROP COLUMN abril;
ALTER TABLE dados DROP COLUMN maio;
ALTER TABLE dados DROP COLUMN junho;
ALTER TABLE dados DROP COLUMN julho;
ALTER TABLE dados DROP COLUMN agosto;
ALTER TABLE dados DROP COLUMN setembro;
ALTER TABLE dados DROP COLUMN outubro;
ALTER TABLE dados DROP COLUMN novembro;
ALTER TABLE dados DROP COLUMN dezembro;

ALTER TABLE dados DROP COLUMN segunda_feira;
ALTER TABLE dados DROP COLUMN terca_feira;
ALTER TABLE dados DROP COLUMN quarta_feira;
ALTER TABLE dados DROP COLUMN quinta_feira;
ALTER TABLE dados DROP COLUMN sexta_feira;
ALTER TABLE dados DROP COLUMN sabado;
ALTER TABLE dados DROP COLUMN domingo;

-----------CONSULTA--------------

select dados.cnpj, dados.razao_social, TO_CHAR(date_table.data_autorizacao, 'DD/MM/YYYY'),
dados.prefixo, dados.descricao, veiculo.tipo_veiculo, sent.sentido,
hora.horario, semanas.segunda_feira, semanas.terca_feira,
semanas.quarta_feira, semanas.quinta_feira, semanas.sexta_feira,
semanas.sabado, semanas.domingo, meses.janeiro, meses.fevereiro,
meses.marco, meses.abril, meses.maio, meses.junho, meses.julho, 
meses.agosto, meses.setembro, meses.outubro, meses.novembro,
meses.dezembro from dados 
join veiculo on veiculo.id = dados.veiculo_id
join hora on hora.id = dados.hr_id
join sent on sent.id = hora.hs_id
join date_table on date_table.id = dados.data_id 
join meses on meses.id = dados.meses_id 
join semanas on dados.semanas_id = semanas.id
order by dados.id;

SELECT
  TABLE_NAME AS nome_tabela,
  (xpath('/row/c/text()', query_to_xml(format('SELECT COUNT(*) AS c FROM %I.%I', table_schema, table_name), FALSE, TRUE, '')))[1]::text::int AS quantidade_registros
  FROM
  ( SELECT
    table_schema,
    TABLE_NAME
    FROM information_schema.tables
    WHERE TABLE_NAME NOT LIKE 'pg_%' AND table_schema IN ('public')
  ) AS tb1;
