
CREATE OR REPLACE VIEW controle_v1 AS 
SELECT voo.id, voo.data_hora_decolagem, voo.data_hora_pouso, (voo.data_hora_pouso - voo.data_hora_decolagem) AS tempo_voo,
voo.aeronave, tipo_aeronave.sigla AS aeronave_sigla, tipo_aeronave.nome AS aeronave_tipo, tipo_aeronave.quant_assentos, 
voo.aeroporto_decolagem, decolagem.nome AS nome_aeroporto_decolagem, decolagem_cidade.nome_cidade AS cidade_decolagem,
decolagem_pais.nome_pais AS pais_decolagem, voo.aeroporto_pouso, pouso.nome AS nome_aeroporto_pouso, 
pouso_cidade.nome_cidade AS cidade_pouso, pouso_pais.nome_pais AS pais_pouso, voo.piloto_id, p_piloto.nome AS piloto_nome,
p_piloto.cpf AS piloto_cpf, p_piloto.sexo AS piloto_sexo, piloto.codigo_anac AS piloto_codigo_anac, 
p_copiloto.nome AS copiloto_nome, p_copiloto.cpf AS copiloto_cpf, p_copiloto.sexo AS copiloto_sexo, 
copiloto.codigo_anac AS copiloto_codigo_anac, 
CASE WHEN pouso_pais.nome_pais = decolagem_pais.nome_pais THEN 0 ELSE 1 END AS internacional
FROM voo
join aeronave on voo.aeronave = aeronave.codigo
join tipo_aeronave on aeronave.tipo_sigla = tipo_aeronave.sigla
join aeroporto AS decolagem on voo.aeroporto_decolagem = decolagem.sigla
join cidade AS decolagem_cidade on decolagem.cidade_id = decolagem_cidade.codigo
join pais AS decolagem_pais on decolagem_cidade.pais_id = decolagem_pais.id
join aeroporto AS pouso on voo.aeroporto_pouso = pouso.sigla
join cidade AS pouso_cidade on pouso.cidade_id = pouso_cidade.codigo
join pais AS pouso_pais on pouso_cidade.pais_id = pouso_pais.id
join piloto on voo.piloto_id = piloto.pessoa_id 
join funcionario AS func_piloto on piloto.pessoa_id = func_piloto.pessoa_id 
join pessoa AS p_piloto on func_piloto.pessoa_id = p_piloto.id
join piloto AS copiloto on voo.copiloto_id = copiloto.pessoa_id 
join funcionario AS func_copiloto on copiloto.pessoa_id = func_copiloto.pessoa_id 
join pessoa AS p_copiloto on func_copiloto.pessoa_id = p_copiloto.id;

\d controle_v1
