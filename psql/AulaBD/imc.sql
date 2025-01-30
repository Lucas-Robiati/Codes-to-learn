CREATE OR REPLACE FUNCTION Fn_IMC(p_number int)
RETURNS numeric(5,2)
AS $$
  DECLARE nome varchar(40); massa_kg numeric(5,2); altura_m numeric(5,2);   
     imc numeric(5,2);
BEGIN
  SELECT givenname || ' ' || surname nome,
     kilograms::numeric(5,2),
     (centimeters::float/100) INTO nome, massa_kg, altura_m
  FROM fakenames
  WHERE number = p_number;
  
  RAISE INFO E'\n  ID: %\n  nome: % \n  massa(kg): % \n altura(metros): %', 
     p_number, nome, massa_kg, altura_m ;
  
  SELECT massa_kg/(altura_m*altura_m) INTO IMC;
  
  RAISE INFO 'IMC: %', imc;
  
  RETURN IMC;
    
END;
$$ LANGUAGE plpgsql;

select number, Fn_IMC(number) FROM fakenames
ORDER BY 2 limit 5;
