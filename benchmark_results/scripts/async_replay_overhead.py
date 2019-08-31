import matplotlib.pyplot as plt
import math
import numpy as np

# Async Replay parameters
cores = ['1', '4', '8', '16', '32']
runs = []

for i in range(1, 11):
    runs.append(str(i))

# Graph parameters
font_size = 20
figure_size = [18, 12]
font = {'family':'serif', 'serif': ['Palatino'],
        'weight' : 'normal',
        'size'   : 30}
width = 0.25

# Graph generation
color_counter = 0
plt.figure(figsize=(figure_size[0], figure_size[1]))
plt.rc('font', **font)
plt.rc('text', usetex=True)
loop = np.arange(5)

times_async_replay = []
times_async_replay_validate = []

for core in cores:
    # Initializing async plot values
    time_async = 0.0
    # Initializing async replay plot values
    time_async_replay = 0.0
    # Initializing async replay validate plot values
    time_async_replay_validate = 0.0

    for run in runs:
        file = '../benchmarks/async_replay/pure_async_replay_' + core + '_200_' + run + '.txt'
        with open(file) as f:
            contents = f.read().splitlines()
            time_async += float(contents[1].split(' ')[-1])
            time_async_replay += float(contents[4].split(' ')[-1])
            time_async_replay_validate += float(contents[7].split(' ')[-1])

    print str(time_async) + ' ' + core

    time_async /= 10.0
    time_async_replay /= 10.0
    time_async_replay_validate /= 10.0

    overhead_async_replay = time_async_replay - time_async
    overhead_async_replay_validate = time_async_replay_validate - time_async

    times_async_replay.append(overhead_async_replay)
    times_async_replay_validate.append(overhead_async_replay_validate)

print times_async_replay
print times_async_replay_validate

plt.bar(loop, times_async_replay, width, label='Async Replay')
plt.bar(loop + width, times_async_replay_validate, width, label='Async Replay Validate')

plt.xticks(loop+width/2, cores, fontsize=28)
plt.legend(loc='best')
plt.ylabel('Amortized overheads per task in us', fontsize=35)
plt.xlabel('Core count', fontsize=35)
plt.yticks(fontsize=28)
plt.grid()
fig_name = 'asyc_replay_overhead.png'
plt.savefig('../graphs/async_replay/' + fig_name, bbox_inches='tight')
plt.close()