SELECT Pessoa.id, Pessoa.nome, Cidade.nome_cidade 
FROM Pessoa LEFT JOIN Cidade ON Cidade_codigo = Cidade.codigo
ORDER BY 1 LIMIT 30;

/*Mesma consulta, anterior usando left e esta usando right join*/
SELECT Pessoa.id, Pessoa.nome, Cidade.nome_cidade 
FROM Cidade RIGHT JOIN Pessoa ON Cidade_codigo = Cidadeq.codigo
ORDER BY 1 LIMIT 30;

CREATE OR REPLACE FUNCTION Fn_CPF(p_ID int)
RETURNS varchar(14)
AS $$
BEGIN
    return CPF 
      FROM pessoa WHERE ID = p_ID;
END;
$$ LANGUAGE plpgsql;

