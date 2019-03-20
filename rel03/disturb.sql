DROP TABLE t_pescador_back;
DROP SEQUENCE t_pescador_seq_id cascade;

CREATE TABLE t_pescador_back AS SELECT * FROM t_pescador ORDER BY random() limit (SELECT (count(*)*0.25)::INTEGER FROM t_pescador);

-- Aqui você cria a sequência em si, que você tá usando como o valor padrão de um id
CREATE SEQUENCE t_pescador_seq_id;
-- Aqui você define o valor inicial da sequência, no seu caso esse valor vai ser 0, no segundo parametro
SELECT setval('t_pescador_seq_id', (SELECT max(tp_id) FROM t_pescador));
ALTER TABLE t_pescador 
-- Aqui você define como padrão o valor da sequencia 
ALTER COLUMN tp_id 
SET DEFAULT nextval('t_pescador_seq_id');
DELETE FROM t_pescador WHERE tp_id IN (SELECT tp_id from t_pescador_back);
INSERT INTO t_pescador (tp_nome, tp_sexo) (SELECT tp_nome, tp_sexo FROM t_pescador_back);
