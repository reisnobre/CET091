from IPython.core.debugger import Tracer
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

l = len(sys.argv)
paths = sys.argv[1:l]

CLIENT = int(paths[0].split('outs/out_t5_')[1].split('x')[0])

clients = [CLIENT]*8
transactions = [1, 15, 30, 45, 60, 75, 90, 100]
latency = []
tps1 = []
tps2 = []


for path in paths:
    with open(path, 'r') as infile:
        line = infile.readlines()[0].split(',')
        latency.append(float(line[0]))
        tps1.append(float(line[1]))
        tps2.append(float(line[2]))

X = np.array(transactions)
Y = np.array(tps1)

plt.title('Relação entre o numero de transações e\n TPS, {} Cliente(s)'.format(CLIENT))
plt.xlabel('Numero de transações')
plt.ylabel('Transações por segundo')
plt.ylim(min(Y), max(Y)+10)
plt.xticks(X, X)

for i,j in zip(X,Y):
        plt.annotate(format(j, '.2f'),xy=(i,j))

slope, intercept, r_value, p_value, std_err = stats.linregress(X,Y)
spearman = stats.spearmanr(X, Y)
correlation = np.corrcoef(X, Y) 
with open ('./{}_t5_client.txt'.format(CLIENT), 'w') as outfile:
    rl = 'slope: {}\nintercept: {}\nr_value: {}\np_value: {}\nstd_err: {}\nspearman: {}\ncorrelation: {}'.format(slope, intercept, r_value, p_value, std_err, spearman, correlation)
    outfile.write(rl)

plt.plot(X,Y, label='Dados')
plt.plot(X, intercept + slope*X, 'r', label='Linha de Regressão')
plt.legend()

plt.savefig('{}_t_client'.format(CLIENT))
