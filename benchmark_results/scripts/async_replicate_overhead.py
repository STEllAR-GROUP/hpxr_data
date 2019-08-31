import matplotlib.pyplot as plt
import math
import numpy as np

# Async replicate parameters
cores = ['1', '4', '8', '16', '32']
n_values = ['3']
runs = []

for i in range(1, 11):
    runs.append(str(i))

# Graph parameters
font_size = 12
figure_size = [18, 12]
font = {'family':'serif', 'serif': ['Palatino'],
        'weight' : 'normal',
        'size'   : 30}
width = 0.20

for n_value in n_values:
    # Graph generation
    color_counter = 0
    plt.figure(figsize=(figure_size[0], figure_size[1]))
    plt.rc('font', **font)
    plt.rc('text', usetex=True)
    loop = np.arange(5)

    times_async_replicate = []
    times_async_replicate_validate = []
    times_async_replicate_vote = []
    times_async_replicate_vote_validate = []

    for core in cores:
        # Initializing async plot values
        time_async = 0.0
        # Initializing async replicate plot values
        time_async_replicate = 0.0
        # Initializing async replicate validate plot values
        time_async_replicate_validate = 0.0
        time_async_replicate_vote = 0.0
        time_async_replicate_vote_validate = 0.0

        for run in runs:
            file = '../benchmarks/async_replicate/pure_async_replicate' + '_' + core + '_200_' + run + '.txt'
            with open(file) as f:
                contents = f.read().splitlines()
                time_async += float(contents[1].split(' ')[-1])
                time_async_replicate_vote_validate += float(contents[-2].split(' ')[-1])
                time_async_replicate_vote += float(contents[-5].split(' ')[-1])
                time_async_replicate_validate += float(contents[-8].split(' ')[-1])
                time_async_replicate += float(contents[-11].split(' ')[-1])

        print str(time_async) + ' ' + str(time_async_replicate) + ' ' + str(time_async_replicate_vote) + ' ' + str(time_async_replicate_vote_validate) + ' ' + str(time_async_replicate_validate)

        time_async_replicate = (time_async_replicate / 3.0 - time_async) / 10.0
        time_async_replicate_validate = (time_async_replicate_validate / 3.0 - time_async) / 10.0
        time_async_replicate_vote = (time_async_replicate_vote / 3.0 - time_async) / 10.0
        time_async_replicate_vote_validate = (time_async_replicate_vote_validate / 3.0 - time_async) / 10.0

        
        times_async_replicate.append(time_async_replicate)
        times_async_replicate_validate.append(time_async_replicate_validate)
        times_async_replicate_vote.append(time_async_replicate_vote)
        times_async_replicate_vote_validate.append(time_async_replicate_vote_validate)

    plt.bar(loop - width, times_async_replicate, width, label='Async replicate')
    plt.bar(loop, times_async_replicate_validate, width, label='Async replicate Validate')
    plt.bar(loop + width, times_async_replicate_vote, width, label='Async replicate Vote')
    plt.bar(loop + 2*width, times_async_replicate_vote_validate, width, label='Async replicate Vote Validate')

    plt.xticks(loop+width/2, cores, fontsize=28)
    plt.yticks(fontsize=28)
    plt.legend(bbox_to_anchor=(0.395, 0.84), loc=2, borderaxespad=0.)
    plt.ylabel('Amortized overheads in us', fontsize=35)
    plt.xlabel('Core count', fontsize=35)
    plt.grid()
    fig_name = 'async_replicate_overhead_' + n_value + '.png'
    plt.savefig('../graphs/async_replicate/' + fig_name, bbox_inches='tight')
    plt.close()