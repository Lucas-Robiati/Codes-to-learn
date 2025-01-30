CREATE OR REPLACE FUNCTION tipo_funcionario(p_prof varchar(1))
RETURNS TABLE
(
  ID int,
  nome varchar(60),
  idade_anos int
)
AS $$
BEGIN
  select upper(p_prof) INTO p_prof;

  if(p_prof = 'A') THEN
        RETURN QUERY
        SELECT pessoa.id, pessoa.nome, DATE_PART(AGE('year',pessoa.data_nasc)) FROM pessoa 
        JOIN funcionario ON pessoa.id = funcionario.pessoa_id
        JOIN aeromoca ON pessoa.id = aeromoca.pessoa_id;
  end if;
 
  if(p_prof = 'P') THEN
        RETURN QUERY
        SELECT pessoa.id, pessoa.nome, DATE_PART(AGE('year',pessoa.data_nasc)) FROM pessoa 
        JOIN funcionario ON pessoa.id = funcionario.pessoa_id
        JOIN piloto ON pessoa.id = piloto.pessoa_id;
  end if;

  if(p_prof = 'G') THEN
        RETURN QUERY
        SELECT pessoa.id, pessoa.nome, DATE_PART(AGE('year',pessoa.data_nasc)) FROM pessoa 
        JOIN funcionario ON pessoa.id = funcionario.pessoa_id
        JOIN gerente ON pessoa.id = gerente.pessoa_id;
  end if;
END;
$$ LANGUAGE plpgsql;
