import subprocess
from IPython.core.debugger import Tracer

PATH = './outs/'
OUT_PATH = '/home/reisnobre/uesc/db_2/benchmark/outs/'
BATCH_SIZE = 10
CLIENTS = [5, 15, 30, 45, 60, 75, 90, 100]
TRANSACTIONS = [1, 15, 30, 45, 60, 75, 90, 100]

def make_csv_batch(client=10, transaction=10):
    body = ''
    lines = ''
    for index in range(1, BATCH_SIZE+1):
        process = subprocess.Popen('pgbench -d -C -c {} -t {} -j 5 benchmark'.format(client, transaction).split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        line = output.decode().split('\n')[8:12]
        lines = lines + make_csv_line(line)
    body = body + make_mean(lines) 
    with open(OUT_PATH + 'out_t5_{}x{}.csv'.format(client, transaction), 'w') as outfile:
        outfile.write(body)

def make_mean(body):
    lines = body.split('\n')[0:BATCH_SIZE]
    latencies = []
    tps_1 = []
    tps_2 = []
    connection = []
    for line in lines:
        latencies.append(float(line.split(',')[0]))
        tps_1.append(float(line.split(',')[1]))
        tps_2.append(float(line.split(',')[2]))
        connection.append(float(line.split(',')[3]))
    print(latencies)
    Tracer()()
    return '{},{},{},{}'.format(sum(latencies)/BATCH_SIZE, sum(tps_1)/BATCH_SIZE, sum(tps_2)/BATCH_SIZE, sum(connection)/BATCH_SIZE)

def make_csv_line(line):
    latency = line[0].split(':')[1].split(' ')[1] 
    tps_1 = line[1].split('=')[1].split(' ')[1]  
    tps_2 = line[2].split('=')[1].split(' ')[1]
    connection = float(tps_2) - float(tps_1)
    return '{},{},{},{},\n'.format(latency, tps_1, tps_2, connection)

def make():
    # for client in CLIENTS:
    #     for transaction in TRANSACTIONS:
    #         make_csv_batch(client, transaction)
    make_csv_batch()

make()
