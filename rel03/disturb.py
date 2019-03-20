import subprocess
import os
import numpy as np
import random

# RESET
BATCH_SIZE = 10
SIZE = 0
HASH = random.getrandbits(128)
DATABASE = 'porto'

experiments = ['no_index', 'cluster', 'reindex', 'vacuum']

popen = subprocess.Popen('rm outs_disturbed/*.txt', shell=True, stdout=subprocess.PIPE, universal_newlines=True)

def querry(q, f, o=2):
    popen = subprocess.Popen('psql -U postgres -d {} -c "{}" {}>>./outs_disturbed/{}.txt'.format(DATABASE, q, o, f), shell=True, stdout=subprocess.PIPE, universal_newlines=True)
    output, error = popen.communicate()
    return error

def corr(target):
    return querry("SELECT correlation FROM pg_stats WHERE tablename = 't_pescador';", target, 1)

def  test_times(target):
    for i in range(BATCH_SIZE):
        querry("SELECT * FROM t_pescador where tp_id = 1831", target)

def process_times(target):
    with open ('./outs_disturbed/{}.txt'.format(target),'r') as infile:
        logs = infile.readlines()
        A = []
        corr = []

        for log in logs[7:len(logs)]:
            A.append(float(log.split()[2]))
        for c in logs[2:5]:
            corr.append(float(c.split()[0]))

        times = np.array(A)
        return times.mean(), corr

results = '===== Test with hash code: {:032x} =====\n\n'.format(HASH)
querry('DROP INDEX tp_id_index;', 'log')
querry('CREATE INDEX tp_id_index ON t_pescador USING btree(tp_id);', 'log')

for e in experiments:
    if e == 'cluster':
        querry('CLUSTER t_pescador USING tp_id_index;', 'log')
        querry('ANALYZE;', 'log')
    elif e == 'reindex':
        querry('REINDEX INDEX tp_id_index;', 'log')
    elif e == 'vacuum':
        querry('VACUUM t_pescador;', 'log')
    if corr(e) is None:
        test_times(e)
        t, c = process_times(e)
        results += '[tp_id, tp_nome, tp_sexo]\n{}, {}, {}\n'.format(c[0], c[1], c[2])
        results += 'Tempo médio: {}\n\n'.format(t)

querry('DROP INDEX t_pescador;', 'log')
results += '\n'
with open('./results_disturbed.txt', 'a') as outfile:
    outfile.write(results)
    results += '{}: {}\n'.format(e, t)

    # test_times('btree')
    # results += '{}: {}\n'.format('btree', process_times('btree'))
    #
    # if corr('cluster') is None:
    #     test_times('cluster')
    #     results += '{}: {}\n'.format('cluster', process_times('cluster'))
    
    # test_times('reindex')
    # results += '{}: {}\n'.format('reindex', process_times('reindex'))
    #
    # test_times('vacuum')
    # results += '{}: {}\n'.format('vacuum', process_times('vacuum'))

    ## FINSISH
      # for i in range(BATCH_SIZE):
#         test()
#
#
#
#
# # DISTUB
#
# # popen = subprocess.Popen('psql -U postgres -d main -f disturb.sql 1>disturb_res.txt', shell=True, stdout=subprocess.PIPE, universal_newlines=True)
