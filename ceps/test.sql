DROP TABLE IF EXISTS endereco;
CREATE TABLE endereco (
  endereco_codigo integer NOT NULL default '0',
  bairro_codigo integer default NULL primary key,
  endereco_cep varchar(9) default NULL,
  endereco_logradouro varchar(72) default NULL,
  endereco_complemento varchar(72) default NULL,
  KEY bairro_codigo (bairro_codigo)
);
create index bairro_codigo on endereco using hash(bairro_codigo);
