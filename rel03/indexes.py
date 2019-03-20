from IPython.core.debugger import Tracer
import subprocess
import os
import numpy as np
import random

# RESET
popen = subprocess.Popen('rm outs/*.txt', shell=True, stdout=subprocess.PIPE, universal_newlines=True)

BATCH_SIZE = 10
SIZE = 0
HASH = random.getrandbits(128)
experiments = ['no_index', 'hash', 'btree']

def querry(q, f):
    popen = subprocess.Popen('psql -U postgres -d main -c "{}" 2>>./outs/{}.txt'.format(q, f), shell=True, stdout=subprocess.PIPE, universal_newlines=True)

def test():
    # drop index
    querry('DROP INDEX cidade_codigo;', 'log')
    # query and catch time for batch_size write to file results
    querry("SELECT * FROM bairro;", 'no_index')
    # create hash index 
    querry('CREATE INDEX cidade_codigo on bairro USING hash(cidade_codigo);', 'log')
    # query and catch time for batch_size write to file results
    querry("SELECT * FROM bairro WHERE cidade_codigo = 16;", 'hash')
    # drop index 
    querry('DROP INDEX cidade_codigo;', 'log')
    # create btree index 
    querry('CREATE INDEX cidade_codigo on bairro USING btree(cidade_codigo);', 'log')
    # query and catch time for batch_size write to file results
    querry("SELECT * FROM bairro WHERE cidade_codigo = 16;", 'btree')
    # drop index 
    querry('DROP INDEX cidade_codigo;', 'log')

def process(target):
    with open ('./outs/{}.txt'.format(target),'r') as infile:
        logs = infile.readlines()
        A = []
        for log in logs:
            A.append(float(log.split()[2]))
        times = np.array(A)
        return times.mean()

for i in range(BATCH_SIZE):
    test()

results = '===== Test with hash code: {:032x} =====\n\n'.format(HASH)
for e in experiments:
    results += '{}: {}\n'.format(e, process(e))

results += '\n'
with open('./results.txt', 'a') as outfile:
    outfile.write(results)

# DISTUB

# popen = subprocess.Popen('psql -U postgres -d main -f disturb.sql 1>disturb_res.txt', shell=True, stdout=subprocess.PIPE, universal_newlines=True)
