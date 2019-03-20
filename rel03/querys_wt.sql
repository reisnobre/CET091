-- Testes sem where, que não se aproveitam dos index

-- Teste sem index
-- CLEANING
drop index cidade_codigo; 
select * from bairro;

-- Teste com hash 
create index cidade_codigo on bairro using hash(cidade_codigo);
select * from bairro;
-- CLEANING
drop index cidade_codigo; 


-- Teste com btree 
create index cidade_codigo on bairro using btree(cidade_codigo);
select * from bairro;

-- Testes com where utilizando o index 
-- Fake EOF

-- Teste sem index
-- CLEANING
drop index cidade_codigo; 
select * from bairro where cidade_codigo = 16;
-- Teste sem index com join
select * from bairro left join cidade on (cidade.cidade_codigo = bairro.cidade_codigo);
select * from cidade left join bairro on (cidade.cidade_codigo = bairro.cidade_codigo);

-- Teste com hash 
create index cidade_codigo on bairro using hash(cidade_codigo);
select * from bairro where cidade_codigo = 16;
-- Teste com btree  com join
select * from bairro left join cidade on (cidade.cidade_codigo = bairro.cidade_codigo);
select * from cidade left join bairro on (cidade.cidade_codigo = bairro.cidade_codigo);

-- CLEANING
drop index cidade_codigo; 

-- Teste com btree 
create index cidade_codigo on bairro using btree(cidade_codigo);
select * from bairro where cidade_codigo = 16;

-- Teste com btree  com join
select * from bairro left join cidade on (cidade.cidade_codigo = bairro.cidade_codigo);
select * from cidade left join bairro on (cidade.cidade_codigo = bairro.cidade_codigo);


