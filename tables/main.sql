drop table TBL_TESTE; 

create table TBL_TESTE (
	TST_COD numeric (4,0),
	TXT_DES varchar(50) not null,
	TXT_SEX char(1) not null check(TXT_SEX in ('F', 'M')),
	TST_SAL numeric(12,2) not null,
	TST_CPF numeric(15,0) not null unique,
	TST_DTA DATE null
);

create index IDX_TST_CPF on TBL_TESTE using hash(TST_CPF);
-- insert into TBL_TESTE values (1, 'A', 'M', 1100, 10010010010, to_date('23/04/2017', 'DD/MM/YYYY'));
-- insert into TBL_TESTE values (2, 'B', 'F', 1200, 20020020020, to_date('23/04/2017', 'DD/MM/YYYY'));
