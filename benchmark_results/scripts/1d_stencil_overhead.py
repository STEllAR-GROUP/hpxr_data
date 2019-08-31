import matplotlib.pyplot as plt
import math
import numpy as np

# dataflow Replay parameters
cores = ['32']
xlabel = ['1D stencil case A\n(32 cores)', '1D stencil case B\n(32 cores)', '1D stencil case A\n(32 cores)', '1D stencil case B\n(32 cores)']
variations = {
    '128': '16000',
    '256': '8000'
}
runs = []

for i in range(1, 11):
    runs.append(str(i))

# Graph parameters
font_size = 12
figure_size = [18, 12]
font = {'family':'serif', 'serif': ['Palatino'],
        'weight' : 'bold',
        'size'   : 40}
width = 0.15

# Graph generation
color_counter = 0
plt.figure(figsize=(figure_size[0], figure_size[1]))
plt.rc('font', **font)
plt.rc('text', usetex=True)
loop = np.arange(2)

x = 0
times_dataflow = []
times_dataflow_replay = []
times_dataflow_replay_validate = []
times_dataflow_replicate = []

for core in cores:

    for tile, subdomain_width in variations.iteritems():

        time_dataflow_replay = 0.0
        time_dataflow_replay_validate = 0.0
        time_dataflow = 0.0
        time_dataflow_replicate = 0.0

        for run in runs:
            file = '../benchmarks/stencil/1d_pure_stencil_' + core + '_' + subdomain_width + '_' + run + '.txt'
            with open(file) as f:
                contents = f.read().splitlines()
                time_dataflow += float(contents[1].split(' ')[-1])
                time_dataflow_replay += float(contents[4].split(' ')[-1])
                time_dataflow_replay_validate += float(contents[7].split(' ')[-1])
                time_dataflow_replicate += float(contents[10].split(' ')[-1])

        times_dataflow.append(time_dataflow / 10.0)
        times_dataflow_replay.append(time_dataflow_replay / 10.0)
        times_dataflow_replicate.append(time_dataflow_replicate / 10.0)
        times_dataflow_replay_validate.append(time_dataflow_replay_validate / 10.0)

    x = 1

plt.bar(loop - width, times_dataflow, width, label='Pure dataflow')
plt.bar(loop, times_dataflow_replay, width, label='Replay without checksums')
plt.bar(loop + width, times_dataflow_replay_validate, width, label='Replay with checksums')
plt.bar(loop + 2 * width, times_dataflow_replicate, width, label='Replicate without\nchecksums')


plt.xticks(loop+width/2, xlabel)
plt.legend(bbox_to_anchor=(0.395, 0.9), loc=2, borderaxespad=0.)
plt.ylabel('Execution time in s', fontsize=40)
plt.xlabel('Number of cores', fontsize=40)
plt.grid()
fig_name = '1d_stencil_overhead.png'
plt.savefig('../graphs/1d_stencil/' + fig_name, bbox_inches='tight')
plt.close()
